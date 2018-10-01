#!/usr/bin/env pypy
import codejam

prob = codejam.Problem()

content = prob.readlines()

n = int(content.pop(0))
for case in range(n):
    rows, cols = map(int, content.pop(0).split(' '))
    grid = []
    for l in range(rows):
        grid.append(list(content.pop(0)))
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '#':
                if (r == rows-1) or (c == cols-1):
                    continue
            else:
                continue
            if (grid[r+1][c] == '#') & (grid[r][c+1] == '#') & (grid[r+1][c+1] == '#'):
                grid[r][c] = '/'
                grid[r+1][c] = '\\'
                grid[r][c+1] = '\\'
                grid[r+1][c+1] = '/'
    output = None
    for row in grid:
        if '#' in row:
            output = "\nImpossible"
    if output is None:
        output = "\n" + "\n".join([''.join(line) for line in grid])
    prob.write_case(output)
print "\n"