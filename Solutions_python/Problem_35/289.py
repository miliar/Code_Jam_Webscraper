import sys, operator

def Find (Vek,Ele):
	for i in range (len(Vek)):
		if Vek[i] == Ele:
			return i
	return -1

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

def Direction (M,P,H,W):
	# 0 = sink
	# 1 = North
	# 2 = West
	# 3 = East
	# 4 = South
	i = P[0]*W+P[1]
	Neigh = [M[i]]
	if P[0]>0: Neigh.append(M[i-W])		# North
	else: Neigh.append(10001)
	if P[1]>0: Neigh.append(M[i-1])		# West
	else: Neigh.append(10001)
	if P[1]<W-1: Neigh.append(M[i+1])	# East
	else: Neigh.append(10001)
	if P[0]<H-1: Neigh.append(M[i+W])	# South
	else: Neigh.append(10001)
	Down,d = min ((x,k) for k,x in enumerate(Neigh))
	return d

def GotoSink (M,LT,P,H,W,L):	# from position P in M (H x W) find the letter (L or old one) and the snake
	p = P[:]
	Let = L
	Snake = [P]
	d = Direction(M,p,H,W)
	while (d != 0) & (Let == L):
		if d == 1:	# North
			p[0] = p[0]-1
		elif d == 2:	# West
			p[1] = p[1]-1
		elif d == 3:	# East
			p[1] = p[1]+1
		else:		# South
			p[0] = p[0]+1
		if LT[p[0]*W+p[1]] != 'N': Let = LT[p[0]*W+p[1]]
		else:
			Snake.append(p[:])
			d = Direction(M,p,H,W)
#	print Let,Snake
	return [Let,Snake]

#MAIN FUNCTION
T = input()
for X in range(1,T+1):
	InList = InputLine()
	H = InList[0]
	W = InList[1]
	Map = []
	for h in range(H):
		InList = InputLine()
		Map.extend(InList)

	LTable = ['N']*H*W
	Letters = 'abcdefghijklmnopqrstuvwxyz0N'
	Pos = [0,0]
	Letter = 0	# 'a'
	while Pos[0]<H:
		if LTable[Pos[0]*W+Pos[1]] == 'N':	# empty cell
			Struc = GotoSink (Map,LTable,Pos,H,W,Letters[Letter])	# returns a letter for the new snake and the snake positions
			for p in Struc[1]:
				LTable[p[0]*W+p[1]] = Struc[0]
				if Struc[0] == Letters[Letter]:	# if the new letter was used, the next will be a new one
					Letter = Letter+1

		Pos[1] = Pos[1]+1
		if Pos[1] >= W:
			Pos[0] = Pos[0]+1
			Pos[1] = 0

	Str = "Case #" + str(X) + ":"
	print Str
	for h in range(H):
		Str = ""
		for w in range(W):
			Str = Str + LTable[h*W+w] + ' '
		print Str
	sys.stdout.flush()
