import sys
import bisect

def get(n):
  return bisect.bisect_right(a, n)

a = list(map(lambda x: int(x.strip()), open('c.ans', 'r').readlines()))
tn = int(sys.stdin.readline())
for t in range(tn):
  l, r = list(map(int, sys.stdin.readline().strip().split(' ')))
  print('Case #%d: %d' % (t + 1, get(r) - get(l - 1)))
