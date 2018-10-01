from common import execute
from collections import defaultdict

T = "T"
X = "X"
O = "O"
EMPTY = "."

def parser(iterator):
	data = []
	for i in xrange(4):
		line = next(iterator).strip()
		data.append(line)
	return data

def solver(data):
	def result(start_x, start_y, dx, dy):
		count = defaultdict(int)
		x, o, empty = 0, 0, 0
		for i in xrange(4):
			cell = data[start_x + i*dx][start_y + i*dy]
			count[cell] += 1
		count[X] += count[T]
		count[O] += count[T]
		if count[X] == 4:
			return "X won", 0
		elif count[O] == 4:
			return "O won", 0
		else:
			return None, count[EMPTY]

	total_empty = 0
	for params in [(0, 0, 1, 0), (0, 1, 1, 0), (0, 2, 1, 0), (0, 3, 1, 0),
	               (0, 0, 0, 1), (1, 0, 0, 1), (2, 0, 0, 1), (3, 0, 0, 1),
	               (0, 0, 1, 1), (3, 0, -1, 1)]:
		winner, num_empty = result(*params)
		if winner:
			return winner
		total_empty += num_empty

	# No winner, check if draw or not completed
	if total_empty == 0:
		return "Draw"
	else:
		return "Game has not completed"

if __name__ == "__main__":
	execute(parser, solver)