class Board(list):
	def __init__(self, *args, **kwargs):
		super(Board, self).__init__(*args, **kwargs)
		self.completed = True

def test_iterable(iterable, char, board):
	for p in iterable:
		if p == char or p == 'T':
			continue
		else:
			if p == '.':
				board.completed = False
			return False
	return True

def test_rows(board, char):
	for row in board:
		if test_iterable(row, char, board):
			return True
	return False

def test_columns(board, char):
	for column in range(4):
		iterable = (board[x][column] for x in range(4))
		if test_iterable(iterable, char, board):
			return True
	return False

def test_diagonals(board, char):
	iterable = (board[i][i] for i in range(4))
	if test_iterable(iterable, char, board):
		return True
	
	iterable = (board[3-i][i] for i in range(4))
	if test_iterable(iterable, char, board):
		return True

def process_test_case():
	board = Board([raw_input().strip() for x in range(4)])

	#eat blank line
	raw_input()
	
	winner = None

	tests = [test_rows, test_columns, test_diagonals]
	for char in ['X', 'O']:
		if any(test(board, char) for test in tests):
			winner = char
			break
	
	if winner:
		return '%s won' % winner
	else:
		if board.completed:
			return 'Draw'
		else:
			return 'Game has not completed'

if __name__ == '__main__':
	T = int(raw_input())
	
	for i in range(T):
		result = process_test_case()

		print 'Case #%i: %s' % (i + 1, result)
