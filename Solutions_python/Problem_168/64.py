import sys
from multiprocessing import Pool

def solve(grid):
  R = len(grid)
  C = len(grid[0])
  rows = [[] for _ in range(R)]
  cols = [[] for _ in range(C)]
  for i in range(R):
    for j in range(C):
      if grid[i][j] != '.':
        rows[i].append(j)
        cols[j].append(i)
  
  result = 0

  for i in range(R):
    for j in range(C):
      if grid[i][j] != '.':
        if len(rows[i]) == 1 and len(cols[j]) == 1: return 'IMPOSSIBLE'
        if grid[i][j] == '^':
          if cols[j][0] == i: result += 1
        elif grid[i][j] == 'v':
          if cols[j][-1] == i: result += 1
        elif grid[i][j] == '<':
          if rows[i][0] == j: result += 1
        else:
          if rows[i][-1] == j: result += 1
  return '{0}'.format(result)


if __name__ == '__main__':
  T = int(input())

  inputs = []

  for iCase in range(T):
    rc = [int(x) for x in input().split(' ')]
    r, c = rc
    grid = []
    for col in range(r):
      l = input()
      grid.append(l)
      
    inputs.append(grid)

  p = Pool(4)

  res = p.map(solve, inputs, 1)
  for iCase, r in enumerate(res):
    print('Case #{0}: {1}'.format(iCase+1, r))
