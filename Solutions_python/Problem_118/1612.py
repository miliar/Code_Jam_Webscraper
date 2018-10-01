import sys
import string
import bisect
inp = sys.stdin
T = int(inp.readline())

def pal(n):
  return str(n) == ''.join(reversed(str(n)))

fns_nums = []
for i in xrange(1, 10**7+1):
  if pal(i):
    ii = i*i
    if pal(ii):
      fns_nums.append(ii)

for cas in xrange(1, T + 1):
  print "Case #%d:" % cas,
  a, b = map(int, inp.readline().strip().split())
  print bisect.bisect_right(fns_nums, b) - bisect.bisect_left(fns_nums, a)
