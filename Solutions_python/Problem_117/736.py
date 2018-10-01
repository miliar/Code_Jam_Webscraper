import os
import sys

def CheckRow(row, height):
  for e in row:
    if e > height:
      return False
  return True

def CheckCase(case, n, m):
  for x in range(m):
    for y in range(n):
      h = case[y][x]
      rh = [case[y][i] for i in range(m)]
      rv = [case[i][x] for i in range(n)]
      if not CheckRow(rh, h) and not CheckRow(rv, h):
        return False
  return True

def ReadCases(inp):
  cases = int(inp.readline())
  for x in range(cases):
    n, m = [int(x) for x in inp.readline().strip().split(' ')]
    case = [[int(x) for x in inp.readline().strip().split(' ')] for y in range(n)]
    yield (case, n, m)

if __name__ == '__main__':
  i = 1
  for c in ReadCases(sys.stdin):
    sys.stdout.write('Case #%s: ' % i)
    if CheckCase(*c):
      sys.stdout.write('YES')
    else:
      sys.stdout.write('NO')
    sys.stdout.write('\n')
    i += 1
