import sys
from fractions import gcd # Euclid to the rescue!

def getint():
  return int(sys.stdin.readline())

def getints():
  return [int(s) for s in sys.stdin.readline().split()]

def solve(ts):
  d = abs(ts[0] - ts[1])
  for t in ts[1:]:
    d = gcd(d, abs(ts[0] - t))
  if all(t % d == 0 for t in ts):
    return 0
  return d - (ts[0] % d)

C = getint()
for i in range(C):
  nums = getints()
  N = nums[0]
  t = nums[1:]
  assert len(t) == N
  print 'Case #%d: %s' % (i+1, solve(t))
