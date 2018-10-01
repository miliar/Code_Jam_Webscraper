#!/usr/bin/env python

import sys, os

def main(*args):

	# Creo el archivo .out
	out_f = open('A.out', 'w')
	
	# Redirecciono el standar output hacia out_f
	old_stdout = sys.stdout
	sys.stdout = out_f

	# Abro el archivo .in
	if len(sys.argv) > 1: in_f = open(sys.argv[1], 'r')
	else: in_f = open('_A.in', 'r')

	# Cargo el numero de casos	
	T = int(in_f.readline())

	# Para cada caso
	for i in range(T):
	
		# Cargo en numero de cables
		N  = int(in_f.readline())
		wires = []
		res = 0
		
		# Cargo la lista de ventanas conectadas por los cables
		for j in range(N):
			line = in_f.readline()
			wires.append(map(int, line.split(" ")))
		
		# Cuento la cantidad de cables que se cruzan
		for v in range(N):
			for u in range(N)[v : ]:
				if  (wires[v][0] < wires[u][0] and wires[v][1] > wires[u][1]) or (wires[v][0] > wires[u][0] and wires[v][1] < wires[u][1]):
					res+=1
		
		# Imprimo el resultado en el archivo .out
		print 'Case #' + str(i+1) + ':', res

	# Cierro el archivo .out
	in_f.close()	
	
	# Restauro el standar output original
	sys.stdout = old_stdout
	
	return 0


#this calls the 'main' function when this script is executed
if __name__ == '__main__': main(sys.argv)
