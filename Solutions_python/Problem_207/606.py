#!/usr/bin/python

import sys

sys.setrecursionlimit(1500)

memo = {}

R = 0
O = 1
Y = 2
G = 3
B = 4
V = 5

a = []

def solve(r, o, y, g, b, v, prev, first, i):
  if r < 0 or o < 0 or y < 0 or g < 0 or b < 0 or v < 0: return False
  if r == 0 and o == 0 and y == 0 and g == 0 and b == 0 and v == 0: return False if prev == first else True
  s = sum([r, y, b])
  if r > (s + 1) / 2 or y > (s + 1) / 2 or b > (s + 1) / 2: return False
  if (r, o, y, g, b, v, prev, first) in memo: return memo[r, o, y, g, b, v, prev, first]
  ans = False
  if prev != 0 and prev != 1 and prev != 5 and solve(r - 1, o, y, g, b, v, R, first, i + 1):
    a[i] = 'R'
    ans = True
  elif prev != 2 and prev != 1 and prev != 3 and solve(r, o, y - 1, g, b, v, Y, first, i + 1):
    a[i] = 'Y'
    ans = True
  elif prev != 4 and prev != 3 and prev != 5 and solve(r, o, y, g, b - 1, v, B, first, i + 1):
    a[i] = 'B'
    ans = True
  memo[r, o, y, g, b, v, prev, first] = ans
  return ans
  
T = int(raw_input())
for t in range(1, T + 1):
  n, r, o, y, g, b, v = map(int, raw_input().split())
  if r > (n + 1) / 2 or y > (n + 1) / 2 or b > (n + 1) / 2:
    print "Case #{}: {}".format(t, 'IMPOSSIBLE')
    continue
  a = [' ' for i in range(n)]
  memo = {}
  if solve(r - 1, o, y, g, b, v, R, R, 1):
    a[0] = 'R'
    print "Case #{}: {}".format(t, ''.join(a).strip())
  elif solve(r, o, y - 1, g, b, v, Y, Y, 1):
    a[0] = 'Y'
    print "Case #{}: {}".format(t, ''.join(a).strip())
  elif solve(r, o, y, g, b - 1, v, B, B, 1):
    a[0] = 'B'
    print "Case #{}: {}".format(t, ''.join(a).strip())
  else:
    print "Case #{}: {}".format(t, 'IMPOSSIBLE')