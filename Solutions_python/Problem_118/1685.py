import sys
from pprint import pprint
import math
from bisect import bisect_right, bisect_left

n = long(sys.stdin.readline())

def find_le(a, x):
    'Find rightmost value less than or equal to x'
    i = bisect_right(a, x)
    if i:
        return i-1
    raise ValueError

def find_ge(a, x):
    'Find leftmost item greater than or equal to x'
    i = bisect_left(a, x)
    if i != len(a):
        return i
    raise ValueError

answers = []
# precompute
end = long(math.ceil(math.sqrt(100000000000000)))
root = long(0)
while root <= end:
  rot = str(root)
  if rot == rot[::-1]:
    num = root*root
    nu = str(num)
    if nu == nu[::-1]:
      answers.append(num)
  root += 1

for i in xrange(n):
  l = map(lambda x: long(x), sys.stdin.readline().split(' '))
  print 'Case #'+str(i+1)+': '+str(find_le(answers, l[1])-find_ge(answers, l[0])+1)


