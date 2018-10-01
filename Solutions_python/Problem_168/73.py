from __future__ import division

T = int(raw_input())

for test in xrange(T):
    R, C = [int(i) for i in raw_input().split()]
    grid = []
    for i in xrange(R):
        grid.append(raw_input())
    ans = 0
    possible = True
    for i in xrange(R):
        for j in xrange(C):
            cell = grid[i][j]
            goes_out = True
            if cell == '^':
                for k in xrange(i):
                    if grid[k][j] != '.':
                        goes_out = False
                        break
            elif cell == '>':
                for k in xrange(j + 1, C):
                    if grid[i][k] != '.':
                        goes_out = False
                        break
            elif cell == 'v':
                for k in xrange(i + 1, R):
                    if grid[k][j] != '.':
                        goes_out = False
                        break
            elif cell == '<':
                for k in xrange(j):
                    if grid[i][k] != '.':
                        goes_out = False
                        break
            else:
                goes_out = False
            if goes_out:
                ans += 1
                alone = True
                for k in xrange(R):
                    if k != i:
                        if grid[k][j] != '.':
                            alone = False
                for k in xrange(C):
                    if k != j:
                        if grid[i][k] != '.':
                            alone = False
                if alone:
                    possible = False
    print "Case #{}: {}".format(test + 1, ans if possible else "IMPOSSIBLE")
