infile = open('in.in', 'r')
outfile = open('out.out', 'w')


def Run():
	T = int(infile.readline())
	for time in range(1, T+1):
		board = [infile.readline() for _ in range(4)]
		result = 'Draw'
		for row in board:
			if(not 'O' in row and not '.' in row):
				result = 'X won'
			elif not 'X' in row and not '.' in row:
				result = 'O won'

		for j in range(4):
			col = ''.join([board[i][j] for i in range(4)])
			if(not 'O' in col and not '.' in col):
				result = 'X won'
			elif not 'X' in col and not '.' in col:
				result = 'O won'

		diag1, diag2 = ''.join(board[i][i] for i in range(4)), ''.join(board[i][3-i] for i in range(4))

		for diag in (diag1, diag2):
			if(not 'O' in diag and not '.' in diag):
				result = 'X won'
			elif not 'X' in diag and not '.' in diag:
				result = 'O won'

		if result == 'Draw' and ('.' in ''.join(row for row in board)):
			result = 'Game has not completed'

		solution = "Case #{}: {}".format(time, result)
		print  solution
		outfile.write(solution + "\n")
		infile.readline()



if __name__ == "__main__":
	Run()
	outfile.close()