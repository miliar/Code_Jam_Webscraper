import sys,os

def readInput(filename):
	f = open(filename)
	lines = f.readlines()
	curentLine = 0
	nrTeste = int(lines[curentLine])
	for testu in range(nrTeste):
		curentLine +=1
		test = lines[curentLine].split()
		C = float(test[0])
		F = float(test[1])
		X = float(test[2])
		rezolva(testu+1,C,F,X)
	f.close()
		
def rezolva(testu,C,F,X):
	f_curent = 2.0
	anterior = 0.0
	timpminim = float(sys.maxsize)
	
	while (1):
		# daca am gasit o timp mai bun decat timpul anterior
		if timpminim > anterior+(X/f_curent):
			timpminim = anterior+(X/f_curent)
			anterior = anterior+C/f_curent
			f_curent += F
		else:
			print "Case #%d: %-.7f" % (testu, timpminim)
			break

readInput("input.txt")                                      
	