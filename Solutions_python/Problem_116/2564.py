from itertools import imap
import re


filename = "in"
f = open(filename, 'r')
lines = f.readlines()
numberOfTestCases = int(lines[0])

class Board:
	def __init__(self, input):
		assert len(input) == 4
		self.board = [row.rstrip('\n') for row in input]
	
	def inv(self):
		return [''.join([row[i] for row in self.board]) for i in range(4)]

	def diagonals(self):
		return [''.join([self.board[i if v > 0 else (i+1)*-1][i] for i in range(4)]) for v in (1,-1)]



	def solve(self):
		asline = ' '.join(self.board)

		# rows
		if re.findall(r"[X|T]{4}", asline):
			return "X won"
		elif re.findall(r"[O|T]{4}", asline):
			return "O won"

		# columns
		asinvertedline = ' '.join(self.inv())
		if re.findall(r"[X|T]{4}", asinvertedline):
			return "X won"
		elif re.findall(r"[O|T]{4}", asinvertedline):
			return "O won"

		# diagonal
		diagonals = ' '.join(self.diagonals())
		if re.findall(r"[X|T]{4}", diagonals):
			return "X won"
		elif re.findall(r"[O|T]{4}", diagonals):
			return "O won"

		elif '.' in asline:
			return "Game has not completed"
		else:
			return "Draw"


for i in range(numberOfTestCases):
	board = lines[i*5+1:i*5+5]
	
	b = Board(board)
	response = b.solve()

	print "Case #%d: %s" % (i+1, response)

