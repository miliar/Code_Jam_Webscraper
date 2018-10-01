def judge(indexes):
	f_o = False
	f_x = False
	n_t = 0
	n_o = 0
	n_x = 0
	#print " ",
	#print indexes
	for pair in indexes:
		if("."==board[pair[0]][pair[1]]):
			return -1
		if("T"==board[pair[0]][pair[1]]):
			n_t+=1
		if("O"==board[pair[0]][pair[1]]):
			if(f_x):
				return -1
			f_o=True
			n_o+=1
		if("X"==board[pair[0]][pair[1]]):
			if(f_o):
				return -1
			f_x=True
			n_x+=1

	if(n_o+n_t > 3):
		return 0
	elif(n_x+n_t > 3):
		return 1
	else:
		return -1

def isFilled():
	for row in board:
		for state in row:
			if("."==state):
				return False
	return True

def judgeRow():
	for i in range(0,4):
		list = [[i,0],[i,1],[i,2],[i,3]]
		if judge(list) != -1:
			return judge(list)
	return -1

def judgeColumn():
	for i in range(0,4):
		list = [[0,i],[1,i],[2,i],[3,i]]
		if judge(list) != -1:
			return judge(list)
	return -1

def judgeDiagonalLeft():
	list = [[0,0],[1,1],[2,2],[3,3]]
	if judge(list) != -1:
		return judge(list)
	return -1

def judgeDiagonalRight():
	list = [[0,3],[1,2],[2,1],[3,0]]
	if judge(list) != -1:
		return judge(list)
	return -1
	
fi = open('input.txt','r')
fo = open('output.txt','w')
t = int(fi.readline())
board = 4*[4*[0]]
for i in range(0,t):
	board[0] = list(fi.readline())
	board[1] = list(fi.readline())
	board[2] = list(fi.readline())
	board[3] = list(fi.readline())
	fi.readline()

	#print board
	if (judgeRow()==0) or (judgeColumn()==0) or (judgeDiagonalLeft()==0) or (judgeDiagonalRight()==0):
		print "Case #{0}: O won".format(i+1)
	if (judgeRow()==1) or (judgeColumn()==1) or (judgeDiagonalLeft()==1) or (judgeDiagonalRight()==1):
		print "Case #{0}: X won".format(i+1)
	if (judgeRow()==-1) and (judgeColumn()==-1) and (judgeDiagonalLeft()==-1) and (judgeDiagonalRight()==-1):
		if isFilled():
			print "Case #{0}: Draw".format(i+1)
		else:
			print "Case #{0}: Game has not completed".format(i+1)

fi.close
fo.close