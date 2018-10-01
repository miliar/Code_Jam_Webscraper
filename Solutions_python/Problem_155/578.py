#!/usr/bin/env python

NOMBRE_ARCHIVO_DE_ENTRADA = "a.in"
NOMBRE_ARCHIVO_DE_SALIDA = "outcome.out"

def imprime(case, texto):
	"""Recibe numero de case y texto que puede ser numero.
	Graba en salida."""
	#print "Case #"+str(case)+": "+str(texto)
	salida.write("Case #"+str(case)+": "+str(texto)+"\n")
	
	
def resuelve(sMax, digitos):
	n = 0
	genteLevantada = 0
	invitados = 0
	
	while True:
		if genteLevantada < n:
			invitados += n - genteLevantada
			genteLevantada += n - genteLevantada
		genteLevantada += int(digitos[n])
		n += 1
		if n > sMax: break

	return invitados
	
def lector():
	entrada = open(NOMBRE_ARCHIVO_DE_ENTRADA, 'r')
	
	for caso in xrange(int(entrada.readline())):
		sMax, digitos = entrada.readline().split()
		
		sMax = int(sMax)
				
		sol = resuelve(sMax, digitos)
		imprime(caso+1, sol)


def main():
	lector()

salida = open(NOMBRE_ARCHIVO_DE_SALIDA, 'w')
main()
salida.close()
