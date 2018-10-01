import sys
import string

def solvebrute(board):
	for i in range(4):
		wonrow = True
		woncolumn = True
		if (board[i][0] != 'T'):
			rowpivot = board[i][0]
		else:
			rowpivot = board[i][1]
		if (board[0][i] != 'T'):
			colpivot = board[0][i]
		else:
			colpivot = board[1][i]
		# can't be a winner if there's a . on the row/column
		if (rowpivot == '.'):
			wonrow = False
			# print 'row was .', i
		if (colpivot == '.'):
			woncolumn = False
			# print 'col was .', i
		for j in range(4):
			if (board[i][j] != rowpivot and board[i][j] != 'T'):
				wonrow = False
				# print i, j, ": wonrow False"
			if (board[j][i] != colpivot and board[j][i] != 'T'):
				woncolumn = False
				# print j, i, ": woncol False"
		if (wonrow):
			# print 'row ', i
			return "{} won".format(rowpivot)
		if (woncolumn):
			# print 'column', i
			return "{} won".format(colpivot)

	# check diagonals
	if (board[0][0] != 'T'):
		diagpivot = board[0][0]
	else:
		diagpivot = board[1][1]
	wondiag = True
	if (diagpivot == '.'):
		wondiag = False
	for i in range(4):
		if (board[i][i] != diagpivot and board[i][i] != 'T'):
			wondiag = False
	if (wondiag):
		# print 'diag '
		return "{} won".format(diagpivot)

	if (board[0][3] != 'T'):
		diag2pivot = board[0][3]
	else:
		diag2pivot = board[1][2]
	wondiag2 = True
	if (diag2pivot == '.'):
		wondiag2 = False
	for el in [board[0][3], board[1][2], board[2][1], board[3][0]]:
		if (el != diag2pivot and el != 'T'):
			wondiag2 = False
	if (wondiag2):
		# print 'diag2'
		return "{} won".format(diag2pivot)

	if (string.find(str(board),'.') >= 0):
		return "Game has not completed"
	else:
		return "Draw"

def printboard(board):
	for row in board:
		print "".join(row)


filename = sys.argv[1]
fin = open(filename, 'r')
cases = int(fin.readline())
board=[['.','.','.','.'],['.','.','.','.'],['.','.','.','.'],['.','.','.','.']]
for case in range(cases):
	for row in range(4):
		board[row] = list(fin.readline().strip())
	fin.readline()
	# printboard(board)
	print "Case #{}: {}".format(case+1, solvebrute(board))
