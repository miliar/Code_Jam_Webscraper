import math
import sys

def getCol(board, col):
	result = []
	for i in range(0,len(board)):
		result.append(board[i][col])
	return result

case = 0

lines = [line.strip() for line in sys.stdin]

lineNumber = 1
while lineNumber < len(lines):

	case = case + 1
	if len(line.strip()) == 0:
		break

	(n,m) = [int(x) for x in lines[lineNumber].split()]
	lineNumber = lineNumber + 1
	rowMax = [0] * n
	colMax = [0] * m

	board = []
	for i in range(0, n):
		board.append([int(x) for x in lines[lineNumber].split()])
		lineNumber = lineNumber + 1

	for row in range(0,n):
		rowMax[row] = max(board[row])

	for col in range(0,m):
		colMax[col] = max(getCol(board, col))

	doable = True
	for row in range(0,n):
		for col in range(0,m):
			if board[row][col] < rowMax[row] and board[row][col] < colMax[col]:
				doable = False
				break

	print "Case #{0}: {1}".format(case, "YES" if doable else "NO")

