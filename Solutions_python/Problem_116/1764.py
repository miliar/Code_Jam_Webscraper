def searchForWinner(board):
	#search horz for X win or O win
	for a in range(4):
		if lineSearch(board[a], "X"):
			return "X won"
		if lineSearch(board[a], "O"):
			return "O won"

	#if no winner, search vert for X win or O win
	for col in range(4):
		column = ""
		for row in range(4):
			column += board[row][col]
		if lineSearch(column, "X"):
			return "X won"
		if lineSearch(column, "O"):
			return "O won"

	#if no winner, search diag for X win or O win
	diag1 = ""
	diag2 = ""
	for a in range(4):
		diag1 += board[a][a]
		diag2 += board[3-a][a]
	if lineSearch(diag1, "X"):
		return "X won"
	if lineSearch(diag1, "O"):
		return "O won"
	if lineSearch(diag2, "X"):
		return "X won"
	if lineSearch(diag2, "O"):
		return "O won"

	#if no winner, find out if board is full:
	if completeGame:
		return "Draw"
	else:
		return "Game has not completed"

def lineSearch(searchString, player):
	searchString = ''.join(searchString)
	#print "Oringinal search string: " + searchString + "\n"

	searchString = searchString.replace("T", player)
	#print "Searching for " + player + " in " + searchString + "\n"

	if player*4 in searchString:
		return True
	else:
		return False

#############
### START ###
#############

f = open("A-large.in", "r")
A = open("A-largeOutput.txt", "w")

T = int(f.readline())
#print "Test Cases (T): " + str(T) +"\n"

for t in range(T):
	board = [["X" for col in range(4)] for row in range(4)]

	completeGame = True
	for row in range(4):
		nextLine = f.readline()
		if '.' in nextLine:
			completeGame = False
		for col in range(4):
			board[row][col] = nextLine[col]

	#print board

	winner = searchForWinner(board)
	print "Case #" + str(t+1) + ": " + winner + "\n"
	A.write("Case #" + str(t+1) + ": " + winner + "\n")

	f.readline()

f.close()
A.close()
