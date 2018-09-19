#!/usr/bin/env python
# -*- coding: iso8859-1 -*-
#
# gcj_round1A_A.py
#
# mariopal
# 7-2008
#
# Using Python 2.5.2 in Linux (Debian Sid):
# $ ./gcj_round1A_A.py input.in > output.out
#
"""
Use: python gcj_round1A_A.py input.in > output.out
"""
# ----------------------------------------------------------------------------
import sys

def out(x):
  sys.stdout.write(str(x))
def out_ln(x):
  sys.stdout.write(str(x) + "\n")
# ----------------------------------------------------------------------------


def test(N, v1, v2):
  v1.sort()
  v2.sort(reverse=True)
  R = 0
  while N:
    N -= 1
    R += v1[N]*v2[N]
  return R
#test


def main():
  if len(sys.argv) > 1:
    inputfile = sys.argv[1]
  else:
    print __doc__
    return

  ftest = open(inputfile, "rb")
  line = ftest.readline()
  numtests = int(line)
  t = 1
  while t <= numtests:
    line = ftest.readline()
    N = line[:-1].split(" ")
    line = ftest.readline()
    vi1 = line[:-1].split(" ")
    v1 = []
    for i in vi1: v1.append(int(i))
    line = ftest.readline()
    vi2 = line[:-1].split(" ")
    v2 = []
    for i in vi2: v2.append(int(i))
    R = test(int(N[0]), v1, v2)
    out_ln("Case #" + str(t) + ": " + str(R))
    t += 1
  ftest.close()
#main


if __name__ == '__main__':
  main()
