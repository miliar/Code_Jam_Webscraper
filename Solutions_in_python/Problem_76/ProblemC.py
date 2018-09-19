from operator import xor
from sys import stdin

def trials(nums):
  if reduce(xor, nums):
    return 'NO'
  else:
    return str(sum(sorted(nums)[1:]))

with open('C:\Users\Erin\Downloads\C-large.in') as inF:
  n = int(inF.readline())
  with open('C-large.out', 'w+') as outF:
    for i in xrange(1, n+1):
      _ = inF.readline()
      nums = map(int, inF.readline().split())
      result = trials(nums)
      print  'Case #%d: %s' % (i, result)
      print  >> outF, 'Case #%d: %s' % (i, result)