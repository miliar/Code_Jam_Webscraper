#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import stdin
from heapq import *

def main():
  n = int(stdin.readline().strip())
  for i in range(n):
    [n, k] = list(map(int, stdin.readline().strip().split(' ')))
    y, z = solve(n, k)
    print("Case #{}: {} {}".format(i+1, y, z))

def solve(n, k):
  if n == k:
    return 0, 0
  h = []
  heappush(h, (-n, 1))
  x = 0
  while True:
    (nl, y) = heappop(h)
    l = -nl
    d = l // 2
    if x + y >= k:
      return d, (d if l % 2 == 1 else (d - 1))
    x += y
    if l % 2 == 0:
      heappush(h, (-d, y))
      heappush(h, (-(d - 1), y))
    else:
      heappush(h, (-d, 2 * y))

if __name__=="__main__":
  main()
