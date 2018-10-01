import fileinput

answers = []
def check(c, arr):
	untilWin = 4
	for i in arr:
		if c == i or i == 'T':
			untilWin -= 1
			if untilWin == 0:
				break
		else:
			untilWin = 4
	return untilWin == 0

def checkRows(c, field):
	result = False
	for row in field:
		if check(c, row):			
			result = True
	# print 'Check rows', result
	return result


def checkColumns(c, field):
	result = False
	for i in range(4):
		column = []
		for j in range(4):
			column.append(field[j][i])
		# print 'Column', column
		if check(c, column):
			result = True
	# print 'Check columns', result
	return result

def checkDiagonals(c, field):
	result = False
	relevantDiagonals = [
		[field[0][0], field[1][1], field[2][2], field[3][3]],
		[field[0][1], field[1][2], field[2][3]],
		[field[1][0], field[2][1], field[3][2]],
		[field[0][3], field[1][2], field[2][1], field[3][0]]]
	for diagonal in relevantDiagonals:
		# print 'Diagonal', diagonal
		if check(c, diagonal):
			result = True
	# print 'Check diagonals', result
	return result

def solveForPlayer(c, field):
	won = checkRows(c, field)
	if not won:
		won = checkColumns(c, field)
		if not won:
			won = checkDiagonals(c, field)
	return won

def solve(field):
	xWon = solveForPlayer('X', field)
	if xWon:
		return 'X won'
	oWon = solveForPlayer('O', field)
	if oWon:
		return 'O won'

	if not xWon and not oWon:
		for row in field:
			for c in row:
				if c == '.':
					return 'Game has not completed'
	return 'Draw'

def readfield(inputlines, firstLineIndex):
	field = []
	for i in range(4):
		rowStr = inputlines[firstLineIndex + i]
		row = []
		for j in rowStr[:-1]:
			row.append(j)
		field.append(row)
	return field

inputlines = []
for line in fileinput.input():
	inputlines.append(line)

numberOfCases = int(inputlines[0])
for i in range(numberOfCases):
	field = readfield(inputlines, 1 + 5 * i)
	result = solve(field);
	answer = 'Case #' + str(i + 1) + ': ' + result + '\n'
	answers.append(answer);

with open ('myfile', 'a') as f:
	for answer in answers:
		f.write (answer)