#!/usr/bin/python
import sys

def gcd(a, b):
  if a < b:
    return gcd(b, a)
  if b == 0:
    return a
  return gcd(b, a%b)

def solve():
  P,Q = map(int, sys.stdin.readline().strip().split('/'))
  d = gcd(P,Q)
  assert(P%d == 0 and Q%d == 0)
  p = P//d
  q = Q//d
  assert(gcd(p,q) == 1)
  if (2**40)%q != 0:
    return "impossible"
  else:
    elves = p * (2**40//q)
    for i in xrange(0, 41):
      if (2**(40-i)) <= elves:
        return i
    print P,Q,p,q
    assert(False)

T = int(sys.stdin.readline())
for test_case in xrange(1, T+1):
  answer = solve()
  print "Case #{0}: {1}".format(test_case, answer)
