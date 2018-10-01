import sys

def get_value(x, y, data):
	return data[y][x]

def check_negative_diag(grid, t):
	if grid[0][3] != t and grid[0][3] != 'T': return False
	if grid[1][2] != t and grid[1][2] != 'T': return False
	if grid[2][1] != t and grid[2][1] != 'T': return False
	if grid[3][0] != t and grid[3][0] != 'T': return False
	return True

def check_positive_diag(grid, t):
	for i in xrange(0,4):
		if grid[i][i] != t and grid[i][i] != 'T':
			return False
	return True

def check_diag(grid, x, y, val):
	if x == y:
		return check_positive_diag(grid, val)
	elif x+y == 3:
		return check_negative_diag(grid, val)
	else:
		return False

def check_col(grid, col, val):
	for r in xrange(4):
		c = grid[r][col]
		if c != val and c!= 'T':
			return False
	return True

def check_row(grid, row, val):
	for c in xrange(4):
		char = grid[row][c]
		if char != val and char != 'T':
			return False
	return True

def check_win(t, grid, x, y):
	if check_row(grid, y, t) or check_col(grid, x, t) or check_diag(grid, x, y, t):
		return True

def determine_outcome(grid):
	ongoing = False
	for r in xrange(4):
		for c in xrange(4):
			val = grid[r][c]
			if val == 'X' or val == 'O':
				if check_win(val, grid, c, r):
					return val + ' won'
			elif val == '.':
				ongoing = True
			c += 1
		r += 1
	if ongoing:
		return 'Game has not completed'
	else:
		return 'Draw'

def load_grid(lines):
	grid = []
	grid.append(list(lines[0]))
	grid.append(list(lines[1]))
	grid.append(list(lines[2]))
	grid.append(list(lines[3]))
	return grid

input_data = sys.stdin.readlines()
T = int(input_data[0])
line = 1

for c in xrange(T) :
	case = c+1
	grid = load_grid(input_data[line:line+4])
	print 'Case #' + str(case) + ': ' + determine_outcome(grid)
	line += 5
	case += 1
