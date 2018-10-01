import operator

def checkDraw(board):
	testBoard = ''.join(board)
	if('.' in testBoard):
		#Game has not completed
		return -1
	#Draw
	return -2
	

def checkStatus(board):
	k = 0
	player = 'X'
	while(k <= 1):
		tempBoard = list(map(operator.methodcaller("replace", 'T', player), board))
		i,j = 0,0
		#Check Vertical Win
		while(i <= 3):
			if(tempBoard[0][i] == tempBoard[1][i] == tempBoard[2][i] == tempBoard[3][i]):
				if(board[0][i] != '.'):
					if(board[0][i] == 'T'):
						return board[1][i]
					else:
						return board[0][i]
			i += 1

		#Check Horizontal Win
		while(j <=3 ):
			if(tempBoard[j][0] == tempBoard[j][1] == tempBoard[j][2] == tempBoard[j][3]):
				if(board[j][0] != '.'):
					if(board[j][0] == 'T'):
						return board[j][1]
					else:
						return board[j][0]
			j += 1
			
		#Check Diagonal Win
		if(tempBoard[0][0] == tempBoard[1][1] == tempBoard[2][2] == tempBoard[3][3]):
			if(tempBoard[0][0] != '.'):
				if(tempBoard[0][0] == 'T'):
					return tempBoard[1][1]
				else:
					return tempBoard[0][0]

		if(tempBoard[0][3] == tempBoard[1][2] == tempBoard[2][1] == tempBoard[3][0]):
			if(tempBoard[0][3] != '.'):
				if(tempBoard[0][3] == 'T'):
					return tempBoard[1][2]
				else:
					return tempBoard[0][3]
		player = 'O'
		k += 1
	return checkDraw(board)

with open('sample.txt') as f:
	tempContent = f.readlines()

content = list(map(str.strip, tempContent))
i = int(tempContent[0])
j = 1
case = 1
writeOutput = open("output.txt", "a")
while i > 0:
	status = checkStatus(content[j:j+4])
	if(status == 'X'):
		status = "X won"
	elif(status == 'O'):
		status = "O won"
	elif(status == -1):
		status = "Game has not completed"
	elif(status == -2):
		status = "Draw"

	writeOutput.write("Case #" + str(case) + ": " + status + "\n");
	case += 1
	j = j + 5
	i = i - 1