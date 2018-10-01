import sys

class Board(object):
	def __init__(self, chose, cards):
		self.chose = chose
		self.cards = cards

	@property
	def choseRow(self):
		return self.cards[self.chose]

	def __str__(self):
		return str((self.chose, self.cards))

class Input(object):
	def __init__(self, boards):
		self.boards = boards

	def run(self):
		choseRows = [set(b.choseRow) for b in self.boards]
		possible = choseRows[0].intersection(choseRows[1])
		return Output(possible)

	def __str__(self):
		return str([str(board) for board in self.boards])

class Output(object):
	def __init__(self, value):
		self.value = value

	def __str__(self):
		if len(self.value) < 1:
			return "Volunteer cheated!"
		elif len(self.value) > 1:
			return "Bad magician!"
		else:
			return str(list(self.value)[0])

def parse_board(lines):
	card = int(lines.next()) - 1
	cards = [[int(i) for i in lines.next().split()] for row in range(4)]
	return Board(card, cards)

def parse(lines):
	return Input([parse_board(lines) for i in range(2)])

def main():
	lines = sys.stdin
	num_cases = int(lines.next())
	for case in range(num_cases):
		result = parse(lines).run()
		print "Case #%d: %s" % (case+1, result)

main()
