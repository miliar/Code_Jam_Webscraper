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

def istidy(n):
  s = str(n)
  return all(s[i] <= s[i+1] for i in range(len(s)-1))

T = read()

for testnum in range(1, T+1):
  N = read()
  while not istidy(N):
    N -= 1
  print("Case #{0}: {1}".format(testnum, N))
