#!/usr/bin/python

import sys, re, string, math

def win(a, b):
    if a<b:
      (b,a) = (a,b)
    k = 1
    while b>0:
      q = a/b
      if q>1:
        return k&1
      (a,b) = (b, a-b)
      k += 1
    return k&1


def do_one_case(cnum):
    w = 0
    (A1, A2, B1, B2) = map(int, sys.stdin.readline().split())
    for a in range(A1, A2+1):
      for b in range(B1, B2+1):
         w += win(a,b)
    print "Case #%d: %d" % (cnum, w)


def main():
    N = int(sys.stdin.readline().strip())
    for i in range(N):
        do_one_case(i+1)


if __name__ == "__main__":
    main()
