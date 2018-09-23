import itertools

def is_ok(r, c, new_grid, known):
    for letter in known:
        row0, row1 = r+1, -1
        col0, col1 = c+1, -1
        for i in xrange(r+1):
            for j in xrange(c+1):
                if grid[i][j] == letter:
                    if i < row0: row0 = i
                    if i > row1: row1 = i
                    if j < col0: col0 = j
                    if j > col1: col1 = j
        for i in xrange(row0, row1 + 1):
            for j in xrange(col0, col1 + 1):
                if grid[i][j] != letter:
                    return False
    return True

def function(r, c, grid):
    unknown = []
    known = set()
    for i in xrange(r+1):
        for j in xrange(c+1):
            if grid[i][j] == '?':
                unknown.append((i,j))
            else:
                known.add(grid[i][j])
    known = list(known)
    for gen in [x for x in itertools.product(known, repeat=len(unknown))]:
        new_grid = list(grid)
        for x in xrange(len(unknown)):
            new_grid[unknown[x][0]][unknown[x][1]] = gen[x]
        if is_ok(r, c, new_grid, known):
            return new_grid

T = int(raw_input().strip())  # read a line with a single integer

for i in xrange(1, T + 1):
    r, c = map(int, raw_input().strip().split(' '))  # read input
    grid = []
    for j in xrange(r):
        grid.append(list(raw_input().strip()))
    output = function(r-1, c-1, grid)        
    print "Case #{}:".format(i)
    for j in output:
        print ''.join(j)
