#! /usr/bin/python

import sys
import pprint

class Grid:
  def __init__(self, m, n, grid):
    self.m = m
    self.n = n
    self.grid = grid

  def find_biggest(self, x, y):
    max_size = min(self.m-x, self.n-y)
    found_size = 1

    for i in xrange(1, max_size):
      for j in xrange(i):
        if self.grid[x+i][y+j] == 9 or self.grid[x+i-1][y+j] == self.grid[x+i][y+j]:
          return found_size
      for j in xrange(i):
        if self.grid[x+j][y+i] == 9 or self.grid[x+j][y+i-1] == self.grid[x+j][y+i]:
          return found_size
      if self.grid[x+i][y+i] == 9 or self.grid[x+i][y+i] != self.grid[x][y]:
        return found_size

      found_size += 1

    return found_size

  def biggest_square(self):
    biggest_size = 0
    biggest_pos = (0, 0)

    for i in xrange(self.m):
      for j in xrange(self.n):
        if self.grid[i][j] != 9:
          tmp = self.find_biggest(i, j)
          if tmp > biggest_size:
            biggest_size = tmp
            biggest_pos = (i, j)

    return (biggest_pos[0], biggest_pos[1], biggest_size)

  def remove_square(self, x, y, size):
    for i in xrange(x, x+size):
      for j in xrange(y, y+size):
        self.grid[i][j] = 9


def solve(m, n, grid):
  my_grid = Grid(m, n, grid)

  squares = [0] * (min(m, n) + 1)

  while True:
    (x, y, size) = my_grid.biggest_square()
    if size != 0:
#      print m, n, x, y, size, squares
      my_grid.remove_square(x, y, size)
      squares[size] += 1
#      pprint.pprint(grid)
    else:
      break

  return squares


fd = open(sys.argv[1])
num_cases = int(fd.readline())

for case in range(0, num_cases):
  (m, n) = [int(item) for item in fd.readline().split(" ")]
  
  grid = []
  for i in xrange(m):
    grid_line = []
    line = fd.readline()
    for j in xrange(n/4):
      tmp = int(line[j], 16)
      grid_line.append((tmp & 8) >> 3)
      grid_line.append((tmp & 4) >> 2)
      grid_line.append((tmp & 2) >> 1)
      grid_line.append(tmp & 1)

    grid.append(grid_line)    

  squares = solve(m, n, grid)
  num = 0
  for i in xrange(min(m, n) + 1):
    if squares[i] != 0:
      num += 1
  print "Case #%d:" % (case+1), num
  for i in xrange(min(m, n), -1, -1):
    if squares[i] != 0:
      print i, squares[i]

