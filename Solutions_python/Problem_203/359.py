#!/usr/bin/env python3

import sys
from copy import deepcopy

EMPTY='?'

def main():
  fi = sys.stdin
  fo = sys.stdout
  case_count = int(fi.readline().strip())
  for i in range(1, case_count+1):
    r, c, grid = read_input(fi)
    solution = solve(r, c, grid)
    display_and_clear(fo, i, solution)

def read_input(f):
  r, c = [int(arg) for arg in f.readline().split()]
  grid = []
  for _ in range(r):
    grid.append(list(f.readline().strip()))
  return r, c, grid

def display_and_clear(f, i, solution):
  grid, r, c = solution
  f.write('Case #%d:\n' % i)
  print_grid(f, grid, r, c)
  f.flush()

def solve(r, c, grid):
  for i in range(r):
    flood_horizontal(grid[i], c)

  flood_vertical(grid, r)

  return grid, r, c

def flood_horizontal(row, c):
  start = 0
  for i in range(c):
    if row[i] == EMPTY:
      start += 1
    else: break

  if start != c:
    last = row[start]

    for i in range(start, -1, -1):
      row[i] = last

    for i in range(start, c):
      if row[i] != EMPTY:
        last = row[i]
      else:
        row[i] = last

def flood_vertical(grid, r):
  start = 0
  for i in range(r):
    if grid[i][0] == EMPTY:
      start += 1
    else: break

  if start != r:
    last = grid[start]

    for i in range(start, -1, -1):
      grid[i] = deepcopy(last)

    for i in range(start, r):
      if grid[i][0] != EMPTY:
        last = grid[i]
      else:
        grid[i] = deepcopy(last)

def print_grid(f, grid, r, c):
  for i in range(r):
    for j in range(c):
      f.write(grid[i][j])
    f.write('\n')

if __name__ == '__main__':
  main()

