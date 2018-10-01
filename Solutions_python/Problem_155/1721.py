#!/usr/bin/env python
import sys
import pdb

def calc(a, motes):
  op = 0
  ops = []
  motes.sort()
  if a == 1:
    return len(motes);
  for i, m in enumerate(motes):
    ops.append(op+(len(motes)-i))
    if a > m:
      a += m
      ops[-1] -= 1
    else:
      while a <= m:
        op += 1
        a += (a-1)
      a += m
  return min(ops)


if __name__ == "__main__":
  if len(sys.argv) > 1:
    ifile = open(sys.argv[1])
  else:
    ifile = sys.stdin
  if len(sys.argv) > 2:
    ofile = open(sys.argv[2])
  else:
    ofile = sys.stdout
  testcases = int(ifile.readline())

  for i in range(testcases):
    n, s = ifile.readline().split(' ')
    s=s[:-1]
    counter = 0
    need = 0
    for (k, c) in enumerate(s):
        if k > counter:
            need += (k-counter)
            counter += (k-counter) # counter = k
        counter += int(c)

    print "Case #%i: %s" % (i+1, str(need))
