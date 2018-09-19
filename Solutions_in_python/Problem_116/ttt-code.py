

def testGrid(grid):
	# X won, O won, Draw, Game has not completed
	for row in grid:
		if testLine(row) != 'inconclusive':
			return testLine(row) + ' won'

	nextGrid = zip(*grid[::-1])
	# print nextGrid
	for row in nextGrid:
		if testLine(row) != 'inconclusive':
			return testLine(row) + ' won'

	diag = [grid[i][i] for i in range(4)]
	diagz = [grid[i][3-i] for i in range(4)]
	# print diag
	# print diagz
	lastGrid = [diag, diagz]
	for row in lastGrid:
		if testLine(row) != 'inconclusive':
			return testLine(row) + ' won'

	for row in grid:
		if '.' in row:
			return 'Game has not completed'
		else:
			return 'Draw'



def testLine(grid):
	sorter = set(grid)
	if sorter == set(['T', 'X']):
		return 'X'
	if sorter == set(['T', 'O']):
		return 'O'
	if sorter == set(['X']):
		return 'X'
	if sorter == set(['O']):
		return 'O'
	return 'inconclusive'


inp = open('A-small-attempt0.in', 'r')
out = open('small-output.txt', 'w')

tests = int(inp.readline()[:-1])

for testNumber in range(tests):
	lines = []
	for i in range(4):
		row = inp.readline()[:-1]
		arrRow = [x for x in row]
		lines.append(arrRow)
	inp.readline()
	# print lines
	writing = 'Case #' + str(testNumber + 1) + ': ' + testGrid(lines) + '\n'
	out.write(writing)