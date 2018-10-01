def check_ver(r, c, grid):
	ct = 0
	dr = r-1
	while dr >= 0 and grid[dr][c] != '#':
		if grid[dr][c] == '-' or grid[dr][c] == '|':
			return -1
		if grid[dr][c] == '.':
			ct += 1
		dr -= 1
	dr = r + 1
	while dr < len(grid) and grid[dr][c] != '#':
		if grid[dr][c] == '-' or grid[dr][c] == '|':
			return -1
		if grid[dr][c] == '.':
			ct += 1
		dr += 1
	return ct

def check_hor(r, c, grid):
	ct = 0
	dc = c-1
	while dc >= 0 and grid[r][dc] != '#':
		if grid[r][dc] == '-' or grid[r][dc] == '|':
			return -1
		if grid[r][dc] == '.':
			ct += 1
		dc -= 1
	dc = c + 1
	while dc < len(grid[0]) and grid[r][dc] != '#':
		if grid[r][dc] == '-' or grid[r][dc] == '|':
			return -1
		if grid[r][dc] == '.':
			ct += 1
		dc += 1
	return ct

def remove_empty_ver(r, c, grid, empty):
	dr = r-1
	while dr >= 0 and grid[dr][c] != '#':
		if grid[dr][c] == '.':
			empty.discard((dr, c))
		dr -= 1
	dr = r + 1
	while dr < len(grid) and grid[dr][c] != '#':
		if grid[dr][c] == '.':
			empty.discard((dr, c))
		dr += 1

def remove_empty_hor(r, c, grid, empty):
	dc = c - 1
	while dc >= 0 and grid[r][dc] != '#':
		if grid[r][dc] == '.':
			empty.discard((r, dc))
		dc -= 1
	dc = c + 1
	while dc < len(grid[0]) and grid[r][dc] != '#':
		if grid[r][dc] == '.':
			empty.discard((r, dc))
		dc += 1


def solve(R, C, grid):
	empty = set([])
	shooters = []
	#print '\n'.join([''.join(grid[r]) for r in xrange(R)])
	for i in xrange(R):
		for j in xrange(C):
			if grid[i][j] == '-' or grid[i][j] == '|':
				shooters.append((i, j))
			if grid[i][j] == '.':
				empty.add((i, j))
	valid = [[] for i in xrange(len(shooters))]
	for i in xrange(len(shooters)):
		r, c = shooters[i]
		hor = check_hor(r, c, grid)
		if hor > -1:
			valid[i].append('-')
		ver = check_ver(r, c, grid)
		if ver > -1:
			valid[i].append('|')
		if hor == 0 and ver == 0:
			valid[i].pop()
	if sum([1 for v in valid if not v]):
		return "IMPOSSIBLE"
	fixed = [i for i in xrange(len(shooters)) if len(valid[i]) == 1]
	var = [i for i in xrange(len(shooters)) if len(valid[i]) == 2]
	for i in fixed:
		r, c = shooters[i]
		if valid[i][0] == '|':
			grid[r][c] = '|'
			remove_empty_ver(r, c, grid, empty)
		else:
			grid[r][c] = '-'
			remove_empty_hor(r, c, grid, empty)
	mx = 2**len(var)
	conf = 0
	while conf < mx:
		emp = empty.copy()
		for i in var:
			r, c = shooters[i]
			if conf & (1 << i):
				grid[r][c] = '|'
				remove_empty_ver(r, c, grid, emp)
			else:
				grid[r][c] = '-'
				remove_empty_hor(r, c, grid, emp)
		conf += 1
		if not emp:
			return "POSSIBLE\n" + '\n'.join([''.join(grid[r]) for r in xrange(R)])
	return "IMPOSSIBLE"


T = int(raw_input())
for case in xrange(1, T+1):
	R, C = map(int, raw_input().split())
	grid = [[c for c in raw_input().strip()] for _ in xrange(R)]
	solution = solve(R, C, grid)
	print "Case #{}: {}".format(case, solution)


