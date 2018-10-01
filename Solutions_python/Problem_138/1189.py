import sys,os,math

def readInput(filename):
	f = open(filename)
	lines = f.readlines()
	curentLine = 0
	nrTeste = int(lines[curentLine])
	for testu in range(nrTeste):
		curentLine += 1
		nrBlocuri = int(lines[curentLine])
		curentLine += 1
		bNaomi = sorted(map(float, lines[curentLine].split()))
		curentLine += 1
		bKen = sorted(map(float, lines[curentLine].split()))
		print "Case #%d:" % (testu+1),
		rezolvaDeceitfulWar(nrBlocuri, bNaomi, bKen)
		rezolvaWar(nrBlocuri,bNaomi,bKen)
	f.close()

def rezolvaDeceitfulWar(nrBlocuri, _bNaomi, _bKen):
	bNaomi = list(_bNaomi)
	bKen = list(_bKen)[::-1] # !!! REVERSED !!!
	#print "DECE\n", nrBlocuri, "\n", bNaomi, "\n", bKen
	pN = 0
	pK = 0
	while len(bNaomi):
		valN = bNaomi[0]
		bNaomi.remove(valN)
		for j in range(len(bKen)):
			valKM = bKen[j]
			valKm = bKen[-1]

			if valN < valKm:
				bKen.remove(valKM)
				pK += 1
				break
			if valN > valKM:
				bKen.remove(valKm)
				pN += 1
				break

			#bKen.remove(valK)
			#if valN<valK:
			#	pK += 1
			#	break
			#else:
			#	pN += 1
			#	break
	#print "DECE: N=",pN," K=",pK
	print pN,
	
def rezolvaWar(nrBlocuri, _bNaomi, _bKen):
	bNaomi = list(_bNaomi)
	bKen = list(_bKen)
	#print "WAR:\n", nrBlocuri, "\n", bNaomi, "\n", bKen
	pN = 0
	pK = 0
	# luam fiecare element de la Naomi
	#for i in range(len(bNaomi)):
	while len(bNaomi):
		valN = bNaomi[0]
		bNaomi.remove(valN)
		removedFromKen = False
		for j in range(len(bKen)):
			valK = bKen[j]
			if valK>valN:
				bKen.remove(valK)
				pK += 1
				removedFromKen = True
				break
		if not removedFromKen:
			bKen.remove(bKen[0])
			pN += 1
	#print "WAR: N=",pN," K=",pK
	print pN

def main():
	if not sys.argv[1]:
		print "da parametru"
		return
	readInput(sys.argv[1])                                      

if __name__ == "__main__":
	main()
