# A small

direction = {
'^' : (-1, 0),
'v' : (1, 0),
'>' : (0, 1),
'<' : (0, -1)
}

def move(r, c, d):
	return (r+d[0], c+d[1])

def does_exit(r, c, d=None):
	if d is None:
		d = direction[grid[r][c]]
	r, c = move(r, c, d)
	while 0 <= r < len(grid) and 0 <= c < len(grid[0]):
		if grid[r][c] != '.':
			return False
		r, c = move(r, c, d)
	return True

def can_be_fixed(r, c):
	for d in direction.itervalues():
		if not does_exit(r, c, d):
			return True
	return False

def lowest_possible(grid):
	must_be_changed = 0
	for r in xrange(len(grid)):
		for c in xrange(len(grid[0])):
			if grid[r][c] != '.' and does_exit(r, c):
				if can_be_fixed(r, c):
					must_be_changed += 1
				else:
					return 'IMPOSSIBLE'
	return must_be_changed






#############################################################

inF = open('input.in')
case_sols = []
for case in xrange(int(inF.readline())):
	R, C = map(int, inF.readline().split())
	grid = []
	for r in xrange(R):
		grid.append(inF.readline().strip())
	case_sols.append(lowest_possible(grid))

inF.close()

outF = open('solution.txt', 'w')
for i, sol in enumerate(case_sols, start=1):
	outF.write('Case #{0}: '.format(i) + str(sol) + '\n')

outF.close()