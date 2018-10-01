#!/usr/bin/env python

import sys

def main():
  f = sys.stdin
  caseCount = int(f.readline().strip())
  for i in xrange(1, caseCount+1):
    r1, g1, r2, g2 = getInput(f)
    count, match = solve(r1, g1, r2, g2)
    displayAndClear(i, count, match)

def getInput(f):
  r1 = int(f.readline().strip())
  g1 = [[int(arg) for arg in f.readline().split()] for i in xrange(4)]
  r2 = int(f.readline().strip())
  g2 = [[int(arg) for arg in f.readline().split()] for i in xrange(4)]
  return r1, g1, r2, g2

def displayAndClear(i, count, match):
  if count < 1:
    print 'Case #%d: %s' % (i, 'Volunteer cheated!')
  elif count > 1:
    print 'Case #%d: %s' % (i, 'Bad magician!')
  else:
    print 'Case #%d: %d' % (i, match)

def solve(r1, g1, r2, g2):
  row1 = g1[r1-1]
  row2 = g2[r2-1]
  count = 0
  match = None
  for card1 in row1:
    if card1 in row2:
      count += 1
      match = card1
  return count, match


if __name__ == '__main__':
  main()

