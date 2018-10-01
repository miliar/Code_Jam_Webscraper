import sys

N = int(sys.stdin.readline())
boardRef = [[0 for i in range(4)] for j in range(4)]


def checkLineXPlus(color, x, y, board):
	if color == 'T' and board[x+1][y] != '.':
		color = board[x+1][y]
	if board[x+1][y] == color or board[x+1][y] == 'T':
		color = board[x+1][y]
		if board[x+2][y] == color or board[x+2][y] == 'T':
			color = board[x+2][y]
			if board[x+3][y] == color or board[x+3][y] == 'T':
				return color
	return False


def checkLineYPlus(color, x, y, board):
	if color == 'T' and board[x][y+1] != '.':
		color = board[x][y+1]
	if board[x][y+1] == color or board[x][y+1] == 'T':
		color = board[x][y+1]
		if board[x][y+2] == color or board[x][y+2] == 'T':
			color = board[x][y+2]
			if board[x][y+3] == color or board[x][y+3] == 'T':
				return color
	return False


def checkLineXPlusYPlus(color, x, y, board):
	if color == 'T' and board[x+1][y+1] != '.':
		color = board[x+1][y+1]
	if board[x+1][y+1] == color or board[x+1][y+1] == 'T':
		color = board[x+1][y+1]
		if board[x+2][y+2] == color or board[x+2][y+2] == 'T':
			color = board[x+2][y+2]
			if board[x+2][y+2] == color or board[x+3][y+3] == 'T':
				return color
	return False


def checkLineXMinusYMinus(color, x, y, board):
	if color == 'T' and board[x-1][y-1] != '.':
		color = board[x-1][y-1]
	if board[x-1][y-1] == color or board[x-1][y-1] == 'T':
		color = board[x-1][y-1]
		if board[x-2][y-2] == color or board[x-2][y-2] == 'T':
			color = board[x-2][y-2]
			if board[x-3][y-3] == color or board[x-3][y-3] == 'T':
				return color
	return False

def checkLineXMinusYPlus(color, x, y, board):
	if color == 'T' and board[x-1][y+1] != '.':
		color = board[x-1][y+1]
	if board[x-1][y+1] == color or board[x-1][y+1] == 'T':
		color = board[x-1][y+1]
		if board[x-2][y+2] == color or board[x-2][y+2] == 'T':
			color = board[x-2][y+2]
			if board[x-3][y+3] == color or board[x-3][y+3] == 'T':
				return color
	return False


def checkline(color, x, y, board):
	if board[x][y] == '.':
		return False

	if x == 0:
		res = checkLineXPlus(color, x, y, board)
		if res:
			return res

	if y == 0:
		res = checkLineYPlus(color, x, y, board)
		if res:
			return res

	if x == 0 and y == 0:
		res = checkLineXPlusYPlus(color, x, y, board)
		if res:
			return res

	if x == 3 and y == 3:
		res = checkLineXMinusYMinus(color, x, y, board)
		if res:
			return res

	if x == 3 and y == 0:
		res = checkLineXMinusYPlus(color, x, y, board)
		if res:
			return res

	return False

for u in range(N):
	boardRef[0] = list(sys.stdin.readline())[:4]
	boardRef[1] = list(sys.stdin.readline())[:4]
	boardRef[2] = list(sys.stdin.readline())[:4]
	boardRef[3] = list(sys.stdin.readline())[:4]

	res = False

	for i in range(4):
		res = checkline(boardRef[i][0],i,0,boardRef)
		if res:
			sys.stdout.write('Case #'+str(u+1)+': '+str(res)+' won\n')
			res = True
			break
	if res:
		sys.stdin.readline()
		continue

	for i in range(4):
		res = checkline(boardRef[0][i],0,i,boardRef)
		if res:
			sys.stdout.write('Case #'+str(u+1)+': '+str(res)+' won\n')
			res = True
			break
	if res:
		sys.stdin.readline()
		continue

	for row in boardRef:
		for c in row:
			if c == '.':
				sys.stdout.write('Case #'+str(u+1)+': Game has not completed\n')
				res = True
				break
		if res:
			break
	if not res:
		sys.stdout.write('Case #'+str(u+1)+': Draw\n')

	sys.stdin.readline()