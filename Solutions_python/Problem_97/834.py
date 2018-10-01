#!/usr/bin/env python
# -*- coding: iso8859-1 -*-
#
# gcj_qualify_C.py
#
# mariopal
# 4-2012
#
# Using Python 2.7.3rc2 in Linux (Debian Sid):
# $ ./gcj_qualify_C.py input.txt > output.txt
#
"""
Use: python gcj_qualify_C.py input.txt > output.txt
"""
# ----------------------------------------------------------------------------
import sys

def out(x):
  sys.stdout.write(str(x))
def out_ln(x):
  sys.stdout.write(str(x) + "\n")
# ----------------------------------------------------------------------------


def is_recycled(n, m):
  sN = str(n)
  sM = str(m)
  if len(sN) != len(sM):  return False

  l = len(sN) - 1
  while l != 0:
    sN = sN[1:] + sN[0]
    if sN == sM:  return True
    l -= 1

  return False
#is_recycled


def test(A, B):
  R = 0
  n = A
  while n <= B:
    m = n+1
    while m <= B:
      if is_recycled(n,m):  R += 1
      m += 1
    n += 1

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
    p = line[:-1].split(" ")
    R = test(int(p[0]),int(p[1]))
    out("\n")
    out_ln("Case #" + str(t) + ": " + str(R))
    t += 1
  ftest.close()
#main


if __name__ == '__main__':
  main()
