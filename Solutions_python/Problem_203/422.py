from __future__ import print_function
s = """3
3 3
G??
?C?
??J
3 4
???A
???B
???C
2 2
CA
KE"""
s = open('A-large.in').read()

import sys
import math

ss = s.split('\n')
T = int(ss[0])

f = open('A.out', 'w')
# f = sys.stdout

idx = 1
for j in range(0, T):
    src = ss[idx].split(' ')
    R, C  = int(src[0]), int(src[1])
    print(R, C)
    grid = []
    for r in range(R):
        row = []
        for c in range(C):
            row.append(ss[idx+r+1][c])
        grid.append(row)

    for c in range(C):
        for r in range(1, R):
            if grid[r-1][c] != '?' and grid[r][c] == '?':
                grid[r][c] = grid[r-1][c]

    for c in range(C):
        for r in range(R - 2, -1, -1):
            if grid[r][c] != '?':
                grid[r][c] = grid[r][c]
            if grid[r+1][c] != '?' and grid[r][c] == '?':
                grid[r][c] = grid[r+1][c]
    for c in range(1, C):
        if grid[0][c] == '?':
            if grid[0][c - 1] != '?':
                for r in range(0, R):
                    grid[r][c] = grid[r][c - 1]
    for c in range(C - 2, -1, -1):
        if grid[0][c] == '?':
            if grid[0][c + 1] != '?':
                for r in range(0, R):
                    grid[r][c] = grid[r][c + 1]

    print('Case #%d:'%(j+1), file=f)
    for r in range(R):
        row = []
        for c in range(C):
            print(grid[r][c],end='',file=f)
        print('', file=f)
    idx += 1+R