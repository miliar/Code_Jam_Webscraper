import itertools

def eventsProbability(ntyped, prob):
	L = list(itertools.product([0,1], repeat=ntyped))
	Pr = []
	for event in L:
		pr = 1
		for i in range(0,ntyped):
			if event[i]==0:
				pr = pr*(1-prob[i])
			else:
				pr = pr*(prob[i])
		Pr.append(pr)
	return L, Pr

def expectedNumber1(ntyped,ntotal,eventsPrb):
	total = 0
	L,Pr = eventsPrb
	for k in range(0,len(L)):
		if (0 not in L[k]):
			total+=(ntotal-ntyped+1)*Pr[k]
		else:
			total+=(ntotal-ntyped+1+ntotal+1)*Pr[k]
	return total

def expectedNumber2(ntyped,ntotal,eventsPrb):
	mintotal = 10000000000000000
	L,Pr = eventsPrb
	for j in range(0,ntyped):
		total = 0
		for k in range(0,len(L)):
			if ( j==ntyped-1 or 0 not in L[k][:ntyped-1-j]):
				total+=(j+1+ntotal-(ntyped-j-1)+1)*Pr[k]
			else:
				total+=(j+1+ntotal-(ntyped-j-1)+1+ntotal+1)*Pr[k]
		if (mintotal>total):
			mintotal = total
	return mintotal

def expectedNumber3(ntyped,ntotal,eventsPrb):
	total = 0
	L,Pr = eventsPrb
	for k in range(0,len(L)):
		total+=(1+ntotal+1)*Pr[k]
	return total

ncases = int(raw_input())

for c in range(0,ncases):
	ntyped, ntotal = raw_input().split()
	ntyped = int(ntyped)
	ntotal = int(ntotal)
	prob = [float(x) for x in raw_input().split()]
	eventsPrb = eventsProbability(ntyped, prob)
	expectedNumbers = [expectedNumber1(ntyped,ntotal,eventsPrb),expectedNumber2(ntyped,ntotal,eventsPrb),expectedNumber3(ntyped,ntotal,eventsPrb)]
	print "Case #%d: %.6f" % (c+1 , min(expectedNumbers))