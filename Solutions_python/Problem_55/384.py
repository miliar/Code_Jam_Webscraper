import sys, operator, string

def Find (Vek,Ele):
	for i in range (len(Vek)):
		if Vek[i] == Ele:
			return i
	return -1

def Insert (Wort, n, s):
	if n not in Wort:
		Wort[n] = s

def InputLine():
	StrLine = sys.stdin.readline()
	L = [StrLine]
	LN = []
	n = 1
	i = Find (StrLine,' ')
	while i >= 0:
		L[n-1:] = [StrLine[:i], StrLine[i+1:]]
		StrLine = StrLine[i+1:]
		n = n+1
		i = Find (StrLine,' ')
	for Str in L:
		LN.append(int(Str))
	return LN

def Umsatz (List,i,k,N):
	j = i
	s = List[i]
	while s <= k:
		j = j+1
		if j==N:
			j = 0
		if j==i:
			return [s,j]
		s = s + List[j]
	s = s - List[j]
	return [s,j]

#MAIN FUNCTION
T = input()
for X in range(1,T+1):
	D = InputLine()
	InitialQ = InputLine()
	Euros = []
	G = 0
	OnextQ = []

	R = D[0]
	k = D[1]
	N = D[2]
	for i in range(N):
		Res = Umsatz (InitialQ,i,k,N)
		Euros.append(Res[0])
		OnextQ.append(Res[1])
	
	#print Euros
	#print OnextQ
	g = 0
	ng = 0
	gAct = []
	yAct = []
	Count = 0
		
	while (ng not in gAct) & (Count < R):
		g = ng
		gAct.append(g)
		ng = OnextQ[g]
		G = G + Euros[g]
		yAct.append(G)
		Count = Count + 1
	
	if Count < R:
		g = ng
		gAct.append(g)
		G = G + Euros[g]
		yAct.append(G)
		Count = Count + 1
		
		Sgam = Find (gAct, ng)
		Fp = G - yAct[Sgam]
		#print Fp, G
		P = Count-1 - Sgam
		#print P, Count, Sgam
		Qp = (R-Count) / P
		Rp = R-Count - Qp*P
		#print Qp, Rp
		G = G + Fp*Qp + yAct[Sgam+Rp] - yAct[Sgam]
		
	Str = "Case #" + str(X) + ":"
	print Str, G
	sys.stdout.flush()
