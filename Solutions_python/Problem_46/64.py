import sys, operator, string

def FindLess (Vek,Ele):
	for i in range (len(Vek)):
		if Vek[i] <= Ele:
			return i
	return -1

def FindLast (Vek,Ele):
	a = 0
	for i in range (len(Vek)):
		if Vek[i] == Ele:
			a = i+1
	return a

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

def OK (M):
	N = len(M)
	A = range (1,N+1)
	for a in A:
		if M[a-1] > a: return False
	return True

#MAIN FUNCTION
T = input()
for X in range(1,T+1):
	N = input()
	A = range (1,N+1)
	M = []
	MA = []
	for r in range(N):
		V = sys.stdin.readline()[:N]
		M.append (FindLast(V,'1'))
		MA.append (M[r]-r-1)
	Y = 0
	if OK (M): Y = 0
	else:
		for a in A:
			One = FindLess (M,a)
			Y = Y + One
			del M[One]

	Str = "Case #" + str(X) + ":"
	print Str, Y
	sys.stdout.flush()
