#Comentário em python

#if em python:
if 5 > 3:
  print("Cinco é maior que 3")

#variáveis python:
x = 7
y = "Jonas"
print(x) #printa a variável
print(y) #printa a variável

#mudança de tipo de variável em python:
x = 4       # x vira do tipo inteiro
x = "Sally" # x virou uma string agora
print(x)

#especificar o tipo da variável:
x = str(3)    # x vai ser '3'
y = int(3)    # y vai ser 3
z = float(3)  # z vai ser 3.0

#dar valor à varias variáveis em uma só linha:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


#assimilar valores à variáveis que estão em uma lista:

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#print de múltiplas variáveis:
x = "Python"
y = "é"
z = "legal"
print(x, y, z)

#input:
# input("Pergunta?")


#soma e subtração
print("Soma e Subtração:")
a = 2
b = 3

print(a + b)
print(a - b)