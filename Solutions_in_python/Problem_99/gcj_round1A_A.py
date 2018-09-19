#!/usr/bin/env python
# -*- coding: iso8859-1 -*-
#
# gcj_round1A_A.py
#
# mariopal
# 4-2012
#
# Using Python 2.7.3rc2 in Linux (Debian Sid):
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


def test(A, B, p):
  R = 0

  C = B - A
  p = map(float, p)
  P = reduce(lambda x, y: x*y, p)
  Q = 1.0 - P

  S1 = (C+1)*P + (C+1+B+1)*Q
  R = S1

  S2 = S1
  for i in range(1, A):
    r = A-i
    P = reduce(lambda x, y: x*y, p[:r])
    Q = 1.0 - P
    S2i = (C+2*i+1)*P  +  (C+2*i+1 + B+1)*Q
    if S2i < S2:  S2 = S2i
  S2i = A + B + 1
  if S2i < S2:  S2 = S2i
  if S2 < R:  R = S2

  S3 = 1 + B + 1
  if S3 < R:  R = S3

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
    AB = line[:-1].split(" ")
    line = ftest.readline()
    p = line[:-1].split(" ")
    R = test(int(AB[0]), int(AB[1]), p)
    out_ln("Case #" + str(t) + ": " + str(R))
    t += 1
  ftest.close()
#main


if __name__ == '__main__':
  main()
