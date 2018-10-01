from sys import stdin
from itertools import product

board = [None] * 4

def check(symbol):
	status = False
	for row in range(4):
		if (board[row][0] == symbol and board[row][1] == symbol
			and board[row][2] == symbol and board[row][3] == symbol):
			status = True
			break

	for col in range(4):
		if (board[0][col] == symbol and board[1][col] == symbol 
			and board[2][col] == symbol and board[3][col] == symbol):
			status = True
			break

	if (board[0][0] == symbol and board[1][1] == symbol 
		and board[2][2] == symbol and board[3][3] == symbol):
		status = True

	if (board[0][3] == symbol and board[1][2] == symbol 
		and board[2][1] == symbol and board[3][0] == symbol):
		status = True

	return status


T = int(stdin.readline())

for case in range(1, T+1):
	for l in range(4):
		board[l] = list(stdin.readline().strip())
		#print board[l]

	# read the empty line
	stdin.readline()

	#locate T
	hasT = False
	for i, j in product(range(4), range(4)):
		if board[i][j] == "T":
			Tloc = (i, j)
			hasT = True
			break

	status = ""
	if not status:
		if hasT:
			board[Tloc[0]][Tloc[1]] = "X"
		if check("X"):
			status = "X won"

	if not status:
		if hasT:
			board[Tloc[0]][Tloc[1]] = "O"
		if check("O"):
			status = "O won"		

	if not status:
		for r, c in product(range(4), range(4)):
			if board[r][c] == ".":
				status = "Game has not completed"
				break

	if not status:
		status = "Draw"

	print "Case #%d: %s" % (case, status)
