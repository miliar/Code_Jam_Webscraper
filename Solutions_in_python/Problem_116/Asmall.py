from numpy import *
fin = open('A-small-attempt2.in','r')
fout = open('TicTacToesol.txt','w')
T = eval(fin.readline())
for i in range(T):
	outputted = False
	square = [[None]*4 for _ in range(4)]
	for j in range(4):
		data = fin.readline()
		data = list(data)
		square[j][0] = data[0]
		square[j][1] = data[1]
		square[j][2] = data[2]
		square[j][3] = data[3]
	if (i!=T-1):
		foo = fin.readline()
	for j in xrange(4):
		a = 0
		b = 0
		c = 0
		e = 0
		f = 0
		g = 0
		h = 0
		k = 0
		q = 0
		for t in xrange(4):
			if ((square[j][t] == 'O') or (square[j][t] =='T')):
				a = a+1
			if ((square[j][t] == 'X') or (square[j][t] =='T')):
				b = b+1
			if ((square[t][j] == 'O') or (square[t][j] == 'T')):
				c = c+1
		 	if ((square[t][j] == 'X') or (square[t][j] == 'T')):
				e = e+1

		if (a == 4):
			if (outputted == False):
				print >> fout, "Case #%d: O won"%(i+1)
				outputted = True			
		if (b==4):
			if (outputted == False):
				print >> fout, "Case #%d: X won" %(i+1)
				outputted = True
		if (c == 4):
			if (outputted == False):
				print >> fout, "Case #%d: O won"%(i+1)
				outputted = True
		if (e == 4):
			if (outputted == False):
				print >> fout, "Case #%d: X won"%(i+1)
				outputted = True
	for j in xrange (4):
		if((square[j][j] == 'O') or (square[j][j] == 'T')):
			f = f+1
		if((square[j][j] == 'X') or (square[j][j] == 'T')):
			g = g+1
		if((square[j][3-j] == 'O') or (square[j][3-j] == 'T')):
			h = h+1
		if((square[j][3-j] == 'X') or (square[j][3-j] == 'T')):	
			k = k+1
	if (h == 4):
		if (outputted == False):
			print >> fout, "Case #%d: O won"%(i+1)
			outputted = True
	if (f==4):
		if (outputted == False):
			print >> fout, "Case #%d: O won"%(i+1)
			outputted = True
	if (k == 4):
		if (outputted == False):
			print >> fout, "Case #%d: X won" %(i+1)
			outputted = True
	if (g == 4):
		if (outputted == False):
			print >> fout, "Case #%d: X won"%(i+1)
			outputted = True
	for j in xrange(4):
		for t in xrange(4):
			if(square[t][j] == '.'):
				if(outputted == False):	
					print >> fout, "Case #%d: Game has not completed" %(i+1)
					outputted = True
			else:
				q=q+1
	if (q==16):
		if (outputted == False):
			print >> fout, "Case #%d: Draw" %(i+1)
			outputted = True
fin.close()
fout.close()