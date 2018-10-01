import os

os.chdir("/Users/Junzologies/Documents/Stuff/Work/2013/Code Jam/Qualification 2013/A")

r=open("A-small-attempt2.in","r")
w=open("A-small-attempt2.out","w")

cases=int(r.readline())

for count in xrange(cases):
	board=[[],[],[],[]]
	done=False
	w.write("Case #"+str(count+1)+": ")
	for x in xrange(4):
		board[x]=list(r.readline().strip())
		dot="." in board[x]

	# Horizontal
	for x in xrange(4):
		ordsum=sum(ord(ch) for ch in board[x])
		if ordsum in [348,352]:
			w.write("X won\n")
			done=True
		elif ordsum in [316,321]:
			w.write("O won\n")
			done=True

	# Vertical
	if not done:
		for x in xrange(4):
			ordsum=0
			for i in xrange(4):
				ordsum+=ord(board[i][x])
			if ordsum in [348,352]:
				w.write("X won\n")
				done=True
			elif ordsum in [316,321]:
				w.write("O won\n")
				done=True
	
	# Diagonal TL-BR
	if not done:
		ordsum=ord(board[0][0])+ord(board[1][1])+ord(board[2][2])+ord(board[3][3])
		if ordsum in [348,352]:
			w.write("X won\n")
			done=True
		elif ordsum in [316,321]:
			w.write("O won\n")
			done=True

	# Diagonal BL-TR
	if not done:
		ordsum=ord(board[3][0])+ord(board[2][1])+ord(board[1][2])+ord(board[0][3])
		if ordsum in [348,352]:
			w.write("X won\n")
			done=True
		elif ordsum in [316,321]:
			w.write("O won\n")
			done=True
	
	if not done:
		if dot:
			w.write("Game has not completed\n")
		else:
			w.write("Draw\n")
	r.readline()
r.close()
w.close()