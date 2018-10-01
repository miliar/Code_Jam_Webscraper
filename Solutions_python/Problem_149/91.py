import math
import itertools
from fractions import gcd

def read_ints():
  return map(int, raw_input().split())

def solve(nums):
  s = sorted(nums)
  ans = 0
  for i in s:
    ind = nums.index(i)
    ans += min(ind, len(nums)-1-ind)
    nums.pop(ind)
  return ans
  
for test in range(1, int(raw_input()) + 1):
  N, = read_ints()
  nums = read_ints()
  sol = solve(nums)
  print "Case #%d: %d" % (test,sol)
  