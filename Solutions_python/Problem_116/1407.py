#!/usr/bin/python
import sys

def calc(lines):
  saw_empty = False
  for i in xrange(0,4):
    for j in xrange(0,4):
      if lines[i][j] == '.':
        saw_empty = True

  for i in xrange(4):
    saw1 = set()
    saw2 = set()
    for j in xrange(4):
      saw1.add(lines[i][j])
      saw2.add(lines[j][i])
    saw1.discard('T')
    saw2.discard('T')
    saw1 = list(saw1)
    saw2 = list(saw2)
    if len(saw1) == 1 and saw1[0] != '.':
      return "%s won" % saw1[0]
    if len(saw2) == 1 and saw2[0] != '.':
      return "%s won" % saw2[0]

  saw1 = set()
  saw2 = set()
  for i in xrange(4):
    saw1.add(lines[i][i])
    saw2.add(lines[i][3-i])
  
  saw1.discard('T')
  saw2.discard('T')
  saw1 = list(saw1)
  saw2 = list(saw2)
  if len(saw1) == 1 and saw1[0] != '.':
    return "%s won" % saw1[0]
  if len(saw2) == 1 and saw2[0] != '.':
    return "%s won" % saw2[0]
 
  return "Game has not completed" if saw_empty else "Draw"

def main():
  d = file(sys.argv[1]).readlines()
  n = int(d[0])
  for j in xrange(n):
    lines = []
    for i in xrange(1,5):
      lines.append(list(d[j*5+i][:-1]))
    print "Case #%d: %s" % (j+1, calc(lines))

main()
