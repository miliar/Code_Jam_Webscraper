from sys import exit, setrecursionlimit
from functools import reduce
from itertools import *
from collections import defaultdict
from bisect import bisect

def read():
  return int(input())

def reads():
  return [int(x) for x in input().split()]

setrecursionlimit(1000000)

T = read()

for testnum in range(1, T+1):
  (D, N) = reads()
  times = []
  for _ in range(N):
    (K, S) = reads()
    times.append((D-K)/S)
  times.sort()
  result = D / times[-1]
  print("Case #{0}: {1}".format(testnum, result))
