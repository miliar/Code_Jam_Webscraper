#!/usr/bin/python
fichero = open("input",'r')
num = int(fichero.readline())

for i in range(num):
	case = "Case #"+str(i+1)+": "
	linea = fichero.readline()
	#empieza
	datos = linea.split(" ")
	numbal = int(datos[0])
	sorp = int(datos[1])
	maxp = int(datos[2])
	punt = []
	for i in range(numbal):
		punt.append(int(datos[3+i]))

	#primero como caso normal
	punts = []
	cont = 0
	pat = (maxp * 3) - 2
	for punto in punt:
		if punto >= pat:
			cont = cont + 1
		else:
			punts.append(punto)

	#luego los casos sorprendentes
	conts = 0
	if sorp > 0:
		pat = pat - 2
		for punto in punts:
			if punto >= pat and punto != 0:
				conts = conts + 1	
	if conts < sorp:
		cont = cont + conts
	else:
		cont = cont + sorp

	print case + str(cont)

