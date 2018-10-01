import sys

def check_board(board):
	# Check the rows
	for row in board:
		s = sum(row)
		if s == 4 or s == 13:
			return "X won"
		elif s == -4 or s == 7:
			return "O won"

	# Check the columns
	for idx in xrange(0, 4):
		column = [row[idx] for row in board]
		s = sum(column)
		if s == 4 or s == 13:
			return "X won"
		elif s == -4 or s == 7:
			return "O won"

	# Check the diagonals
	diag1 = [board[i][i] for i in xrange(0, 4)]
	diag2 = [board[3-i][i] for i in xrange(0, 4)]
	s = sum(diag1)
	if s == 4 or s == 13:
		return "X won"
	elif s == -4 or s == 7:
		return "O won"
	s = sum(diag2)
	if s == 4 or s == 13:
		return "X won"
	elif s == -4 or s == 7:
		return "O won"
	
	return "Game has not completed"


def main(argv):
	f = open(argv[0])
	out = open('out.txt', 'w')

	T = int(f.readline())

	_mapping = {
		'X' : 1,
		'O' : -1,
		'T' : 10,
		'.' : 0
	}
	for case in xrange(0, T):
		original_board = [list(f.readline().strip()) for _ in xrange(0, 4)]
		f.readline() # read the blank

		full_rows = 0
		for row in original_board:
			try:
				row.index('.')
				break
			except ValueError, e:
				full_rows += 1

		board = [[_mapping[char] for char in row] for row in original_board]
		ret = check_board(board)
		if full_rows == 4 and ret == "Game has not completed":
			out.write("Case #%d: %s\n" % (case + 1, "Draw"))
		else:
			out.write("Case #%d: %s\n" % (case + 1, ret))

	f.close()
	out.close()


if __name__ == "__main__":
	sys.exit(main(sys.argv[1:]))