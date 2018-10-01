from sys import exit, setrecursionlimit
from functools import reduce
from itertools import *
from collections import defaultdict
from bisect import bisect
from heapq import heappush, heappop, heapify

def read():
  return int(input())

def reads():
  return [int(x) for x in input().split()]

def argmax(xs):
  return xs.index(max(xs))

setrecursionlimit(1000000)

T = read()
imp = "IMPOSSIBLE"

for testnum in range(1, T+1):
  (N, Q) = reads()
  E = [0] * N; S = [0] * N
  for i in range(N):
    (E[i], S[i]) = reads()

  D = []
  for i in range(N):
    D.append(reads())

  U = [0] * Q; V = [0] * Q
  for j in range(Q):
    (U[j], V[j]) = reads()

  pos = [0] * N
  for i in range(1, N):
    pos[i] = pos[i-1] + D[i-1][i]

  INF = 10**20
  dp = [INF] * N
  dp[0] = 0
  for i in range(1, N):
    for j in range(i):
      d = pos[i]-pos[j]
      if E[j] >= d:
        dp[i] = min(dp[i], dp[j] + d / S[j])
  result = dp[-1]

  print("Case #{0}: {1}".format(testnum, result))
