#!/usr/bin/python
import optparse
import sys

def gcd(a, b):
	if a == 0:
		return abs(b)
	return abs(gcd(b % a, a))

def optimum_anniversary(N, t):
  # first of all, observe that we have
  #   gcd(y+t1, ..., y+tn) = gcd(y+t1, t2-t1, ..., tn-t1) = gcd(y+t1, d)
  # where d is the gcd of t2-t1, ..., tn-t1, so let's compute d...
  t1 = t[0]
  d = reduce(gcd, [x - t1 for x in t[1:]], 0)
  
  # we ought to find the *minimal* y >= which maximises
  #   gcd(y+t1, d)
  # we may suppose that t1 < d...
  t1 = t1 - (t1/d)*d
  
  # then the optimal result is achieved for y+t1 = 0, if possible, else for y+t1 = d, i.e....
  return 0 if t1 == 0 else d-t1
  
parser = optparse.OptionParser()
parser.add_option("--fast", action="store_true", dest="fast")
opts, _ = parser.parse_args()

readline = sys.stdin.readline
C = long(readline())
for c in range(C):
  t = map(long, readline().split(' '))
  N = t[0]
  t = t[1:]
  y = optimum_anniversary(N, t)
  print "Case #%i: %s" % (c+1, y)