N = int( raw_input().strip() )

def getBoard() :
	ret = [""]*4
	for y in xrange(4) :
		ret[y] = raw_input().strip()
	return ret

def checkWin(b, c) :
	for i in xrange(4) :
		flag1 = True
		flag2 = True
		for j in xrange(4) :
			if b[i][j] != c and b[i][j] != "T" :
				flag1 = False
			if b[j][i] != c and b[j][i] != "T" :
				flag2 = False
		if flag1 or flag2 :
			return 1
	
	flag1 = True
	flag2 = True
	for i, j in zip(xrange(4), xrange(4)) :
		if b[i][j] != c and b[i][j] != "T" :
			flag1 = False
	for i, j in zip(xrange(4), xrange(3, -1, -1) ) :
		if b[i][j] != c and b[i][j] != "T" :
			flag2 = False
	if flag1 or flag2 :
		return 1

	return 0

def checkStatus(b) :
	if checkWin(b, "X") == 1 :
		return "X won"
	elif checkWin(b, "O") == 1:
		return "O won"
	else :
		flag = True
		for i in xrange(4) :
			for j in xrange(4) :
				if b[i][j] == "." :
					flag = False
					break
		if flag :
			return "Draw"
	return "Game has not completed"


for i in xrange(N) :
	if i!=0 : raw_input()
	board = getBoard()
	status = checkStatus(board)
	print "Case #" + str(i+1) + ": " + status