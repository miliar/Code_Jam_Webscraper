import sys

def madnbad (board, boardT, i, j):
	return board[i][j] < max(board[i]) and board[i][j] < max(boardT[j])

def isnoob (board, boardT):
	for i in xrange(len(board)):
		for j in xrange(len(board[0])):
			if madnbad(board, boardT, i, j):
				return "NO"
	return "YES"

def main():
	t = int(sys.stdin.readline())
	for i in range(t):
		dims = map(int, sys.stdin.readline().split(' '))
		board = []
		boardT = []
		for j in range(dims[0]):
			board.append(map(int, sys.stdin.readline().split(' ')))

		boardT = [[x[k] for x in board] for k in range(dims[1])]

		print "Case #" + str(i+1) + ": " + isnoob(board, boardT)

if __name__ == "__main__":
	main()