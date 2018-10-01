#!/usr/bin/env python3
# c - cookie farm cost
# f - cookie farm return rate
# x - number of cookies
# p - number of farms to purchase
# r - cookie gain rate
import itertools
def cookietime(c, f, x, p):
  r = 2
  s = 0
  while True:
    if p == 0:
      return s + x/r
    else:
      s += c/r
      p -= 1
      r += f

def mintime(c, f, x):
  lt = None
  i = 0
  for p in itertools.count():
    t = cookietime(c, f, x, p)
    if lt == None or t < lt:
      lt = t
    else:
      return lt

if __name__ == '__main__':
  cases = int(input())
  for case in range(1, cases+1):
    c, f, x = tuple(float(i) for i in input().split(' '))
    out = mintime(c, f, x)
    print("Case #%d: %.7f" % (case, out))
