#!/usr/bin/python
fichero1 = open("entrada",'r')
fichero2 = open("salida",'r')
fichero3 = open("small",'r')
dic = {}
lista = []

for frase in fichero1:
	frase2 = fichero2.readline()
	for i in range(len(frase)):
		dic[frase[i]] = frase2[i]

for frase in fichero3:
	for letra in frase:
		for e in dic.keys():
			if letra == e:
				letra = dic[e]				
				lista.append(letra)
				break
			elif letra == "q":
				letra = "z"
				lista.append(letra)
				break
			elif letra == "z":
				letra = "q"
				lista.append(letra)
				break
			

salida = "Case #0: "
cont = 1
for letra in lista:
	
	salida = salida  + letra
	if letra == "\n":
		cont = cont + 1
		salida = salida + "Case #"+str(cont)+": "
	

print salida
print dic
		


