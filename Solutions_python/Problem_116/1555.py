#!/usr/bin/env python



salida = open("salida.out", 'w')



def imprime(case, texto):
	"""Recibe numero de case y texto que puede ser numero.
	Graba en salida."""
	
	
	salida.write("Case #"+str(case)+": "+str(texto)+"\n")


class Tablero(object):
	def __init__(self):
		self.tablero = []
				
	def imprimir_tablero(self):
		print self.tablero
	
	def agrega_linea(self, linea):
		self.tablero.append(linea)
		
	def revisa_diagonales(self):
		primerCasillero = self.tablero[0][0]
		if primerCasillero == "T":
			primerCasillero = self.tablero[1][1]
		
		gano = False
		#Primera diagonal
		for x in xrange(1,4):
			if primerCasillero == ".": break
			posicionAComparar = self.tablero[x][x]
			if posicionAComparar == primerCasillero or posicionAComparar == "T":
				if x == 3: gano = True
				continue
			else:
				break
		
		if gano:
			return primerCasillero+" won"
		
		#segunda diagonal		
		primerCasillero = self.tablero[0][3]
		if primerCasillero == ".": return None
		if primerCasillero == "T":
			primerCasillero = self.tablero[1][2]
			
		for x in xrange(1,4):
			posicionAComparar = self.tablero[x][3-x]
			if posicionAComparar == primerCasillero or posicionAComparar == "T":
				if x == 3: gano = True
				continue
			else:
				break
		
		if gano:
			return primerCasillero+" won"
		return None
			
	
	def revisa_filas(self):
		for x in xrange(4):
			ganador = self.revisa_fila(x)
			if ganador: return ganador
		
		
	def revisa_fila(self, numeroDeFila):
		primerCasillero = self.tablero[numeroDeFila][0]
		if primerCasillero == ".": return None
		if primerCasillero == "T":
			primerCasillero = self.tablero[numeroDeFila][1]
		
		gano = False
		for x in xrange(1,4):
			posicionAComparar = self.tablero[numeroDeFila][x]
			if posicionAComparar == primerCasillero or posicionAComparar == "T":
				if x == 3: gano = True
				continue
			else:
				break
		
		if gano:
			return primerCasillero+" won"
		return None
		
	def revisa_columnas(self):
		for x in xrange(4):
			ganador = self.revisa_columna(x)
			if ganador: return ganador
		
		
	def revisa_columna(self, numeroDeColumna):
		primerCasillero = self.tablero[0][numeroDeColumna]
		if primerCasillero == ".": return None
		if primerCasillero == "T":
			primerCasillero = self.tablero[1][numeroDeColumna]
		
		gano = False
		for x in xrange(1,4):
			posicionAComparar = self.tablero[x][numeroDeColumna]
			if posicionAComparar == primerCasillero or posicionAComparar == "T":
				if x == 3: gano = True
				continue
			else:
				break
		
		if gano:
			return primerCasillero+" won"
		return None
	
	def juego_terminado(self):
		terminado = True
		for x in xrange(4):
			for y in xrange(4):
				if self.tablero[x][y] == ".":
					terminado = False
					return terminado
					
		return terminado
				
	def resultado(self):
		primerCasillero = self.tablero[0][0]
		ganador = None
		
		ganador = self.revisa_diagonales()
		if ganador: return ganador
		ganador = self.revisa_filas()
		if ganador: return ganador
		ganador = self.revisa_columnas()
		if ganador: return ganador
		
		#no gano nadie. Termino?
		if self.juego_terminado(): return "Draw"
		return "Game has not completed"
				 
				

def lector():
	entrada = open("a.in", 'r')
	
	for numero_de_tablero in xrange(int(entrada.readline())):
		#crea tablero
		tablero = Tablero()
		for x in xrange(4):
			tablero.agrega_linea(entrada.readline()[0:4])
	
		#salteo linea en blanco
		entrada.readline()
		
		#evalua
		resultado = tablero.resultado()

		imprime(numero_de_tablero+1, resultado)
	

def main():
	lector()

main()
salida.close()










