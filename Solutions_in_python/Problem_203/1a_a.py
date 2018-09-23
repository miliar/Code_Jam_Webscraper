from collections import defaultdict
from fractions import Fraction as F

T = int(input().strip())

for t in range(1, T+1):
    R, C = map(int, input().strip().split(' '))
    grid = []
    inits = {}
    for r in range(R):
        grid.append(list(input().strip()))
        for c in range(C):
            if grid[r][c] != '?': inits[grid[r][c]] = (r, c)
    #print(inits)
    # Let's try greedy
    for i in inits:
        ulr, ulc = inits[i]
        lrr, lrc = inits[i]
        # Go left
        while ulc > 0 and grid[ulr][ulc-1] == '?':
            ulc -= 1
        # Go right
        while lrc < (C-1) and grid[lrr][lrc+1] == '?':
            lrc += 1
        # Go up
        while ulr > 0 and all([x == '?' for x in grid[ulr-1][ulc:lrc+1]]):
            ulr -= 1
        while lrr < (R-1) and all([x == '?' for x in grid[lrr+1][ulc:lrc+1]]):
            lrr += 1
        # Fill in grid
        #print(i,ulr,ulc,lrr,lrc)
        for r in range(ulr, lrr+1):
            for c in range(ulc, lrc+1):
                grid[r][c] = i
    print('Case #%d:' % (t,))
    for row in grid:
        print(''.join(row))
    