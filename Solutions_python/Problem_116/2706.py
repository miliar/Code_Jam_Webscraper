#!/usr/bin/env python

def check(i0, j0, di, dj):
  p = grid[i0][j0]
  if p == '.':
    return
  if p == 'T':
    p = grid[i0 + di][j0 + dj]
  for n in xrange(4):
    i = i0 + di*n
    j = j0 + dj*n
    if grid[i][j] != p and grid[i][j] != 'T':
      return
  return p

for cse in xrange(1, int(raw_input()) + 1):
  grid = [raw_input() for _ in xrange(4)]
  try:
    raw_input()
  except EOFError:
    pass

  winner = None
  winner
  for i in xrange(4):
    winner = check(0, i, 1, 0)
    if winner:
      break
    winner = check(i, 0, 0, 1)
    if winner:
      break
    winner = check(0, 0, 1, 1)
    if winner:
      break
    winner = check(0, 3, 1, -1)
    if winner:
      break

  if winner:
    result = '{} won'.format(winner)
  else:
    result = 'Draw'
    for row in grid:
      if '.' in row:
        result = 'Game has not completed'
        break

  print 'Case #{}: {}'.format(cse, result)
