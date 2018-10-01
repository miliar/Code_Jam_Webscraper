import sys
def won(board, c):
	for line in board:
		if line.replace('T',c) == 4*c:
			return True
	if "".join(board[i][i] for i in range(4)).replace('T',c) == 4*c:
		return True

T = int(sys.stdin.readline())
for t in range(T):
	board = [sys.stdin.readline().strip() for _ in range(4)]
	res = ""
	for c in ('X', 'O'):
		if won(board, c) or won(map("".join,zip(*board[::-1])), c):
			res = "%s won" % c
			break
	else:
		if '.' in "".join(board):
			res = "Game has not completed"
		else:
			res = "Draw"
	print "Case #%d: %s" % (t+1, res)
	sys.stdin.readline()
