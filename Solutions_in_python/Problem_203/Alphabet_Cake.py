#!/bin/python3

T = int(input().strip())
for test in range(T):
    R, C = [int(x) for x in input().split()]
    grid = []
    for i in range(R):
        row = list(input().strip())
        grid.append(row)

    emptyrows = []
    nonemprows = []
    for rowind, row in enumerate(grid):
        if all(x == '?' for x in row):
            emptyrows.append(rowind)
        else:
            nonemprows.append(rowind)
            marker = next(x for x in row if x != '?')
            for i in range(C):
                if row[i] == '?':
                    row[i] = marker
                else:
                    marker = row[i]

    # now fill empty rows
    for i in emptyrows:
        copyfrom = min(nonemprows, key=lambda x: abs(x - i))
        for j in range(C):
            grid[i][j] = grid[copyfrom][j]

    print('Case #%d:' % ((test + 1)))
    for row in grid:
        print (''.join(row))
