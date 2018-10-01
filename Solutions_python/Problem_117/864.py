#! /usr/bin/python

from sys import argv,exit

def check_columna(case,col,el):
	for fila in case:
		if fila[col] > el:
			return False
	return True

def analizar_linea(case):
	for fila,line in enumerate(case):
		maximo = max(line)
		for col, el in enumerate(line):
			if el < maximo:
					if not check_columna(case,col,el):
						return "NO"
	return "YES"

if len(argv) != 3:
	print "Usage: prog <filein> <fileout>"
	exit(0)

filein = open(argv[1],"r")
fileout = open(argv[2],"w")

lines = filein.read().split("\n")
nlines = int(lines[0])
x = 1

for i in range(1,nlines+1):
	dim = [int(a) for a in lines[x].split(" ")]

	case = []
	for l in lines[x+1:x+dim[0]+1]:
		case.append([int(t) for t in l.split(" ")])

	fileout.write("Case #" + str(i) + ": ")
	fileout.write(analizar_linea(case) + "\n")

	x = x + dim[0] + 1
