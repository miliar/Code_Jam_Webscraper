#!/usr/bin/python
from heapq import *

def calc(h, k):
  while k >= 1:
    a = heappop(h)
    b = -(-a // 2)
    if a % 2 == 0:
      c = b + 1
    else:
      c = b
    if k == 1:
      return (-b, -c)
    heappush(h, b)
    heappush(h, c)
    k -= 1

t = int(raw_input())
for i in range(1, t+1):
   (n, k) = map(int, raw_input().split())
   h = [-n]
   (maxn, minm) = calc(h,k)
   print "Case #%s: %i %i" % (i, maxn, minm)
