from sys import exit, setrecursionlimit
from functools import reduce
from itertools import *
from collections import defaultdict
from bisect import bisect
from heapq import heappush, heappop

def read():
  return int(input())

def reads():
  return [int(x) for x in input().split()]

setrecursionlimit(1000000)

T = read()

for testnum in range(1, T+1):
  (N, K) = reads()
  hp = [-N]
  for _ in range(K):
    x = -heappop(hp)
    (q, m) = divmod(x-1, 2)
    heappush(hp, -q)
    heappush(hp, -(q+m))

  print("Case #{0}: {1} {2}".format(testnum, q+m, q))
