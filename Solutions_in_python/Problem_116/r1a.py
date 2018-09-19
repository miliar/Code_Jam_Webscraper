import os
import sys

def CheckRow(row):
  # Sorts into '.', 'O', 'T', 'X'
  row = sorted(row)
  if row[0] == '.':
    return '.'
  elif row[0] == 'O' and (row[3] == 'O' or row[3] == 'T'):
    return 'O'
  elif (row[0] == 'T' or row[0] == 'X') and row[3] == 'X':
    return 'X'
  else:
    return 'T'

def Check(case, x, y, dx, dy):
  return CheckRow([case[x+(dx*i)][y+(dy*i)] for i in range(0,4)])

def ReadCases(inp):
  cases = int(inp.readline())
  for x in range(cases):
    case = [list(inp.readline().strip()) for x in range(0,4)]
    yield case
    inp.readline()

def ReadResults(case):
  for x in range(0,4):
    yield Check(case, x, 0, 0, 1)
  for y in range(0,4):
    yield Check(case, 0, y, 1, 0)
  yield Check(case, 0, 0, 1, 1)
  yield Check(case, 3, 0, -1, 1)

if __name__ == '__main__':
  i = 1
  for c in ReadCases(sys.stdin):
    results = sorted([r for r in ReadResults(c)])
    #print results
    sys.stdout.write('Case #%s: ' % i)
    if 'X' in results:
      sys.stdout.write('X won')
    elif 'O' in results:
      sys.stdout.write('O won')
    elif results[0] == 'T' and results[-1] == 'T':
      sys.stdout.write('Draw')
    elif results[0] == '.':
      sys.stdout.write('Game has not completed')
    else:
      raise RuntimeError("Should have come to a conclusion!")
    i += 1
    sys.stdout.write('\n')
    #print results

