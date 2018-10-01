#!/usr/bin/python

import os
import sys

def gen_grid(n, A, B, C, D, x0, y0, M):
  g = [[0, 0, 0] for x in xrange(3)]
  X = x0; Y = y0
  g[X%3][Y%3] += 1
  for i in xrange(1, n):
    X = (A*X + B)%M
    Y = (C*Y + D)%M
    g[X%3][Y%3] += 1
  return g



def count_tri(g):
  cnt = 0
  for i in xrange(3):
    for j in xrange(3):
      n = g[i][j]
      if n >= 3:
        cnt += n*(n - 1)*(n - 2)/6
  for i in xrange(3):
    for j in xrange(3):
      n1 = g[i][j]
      if n1 >= 2:
        i2 = (6 - 2*i)%3
        j2 = (6 - 2*j)%3
        if i2==i and j2==j:
          continue
        cnt += n1*(n1 - 1)/2*g[i2][j2]
  cnt2 = 0
  for i in xrange(9):
    for j in xrange(i + 1, 9):
      for k in xrange(j + 1, 9):
        if (i//3 + j//3 + k//3)%3 != 0 or (i + j + k)%3 != 0:
          continue
        cnt2 += g[i//3][i%3]*g[j//3][j%3]*g[k//3][k%3]
  return cnt + cnt2


def run(inf):
  N = int(inf.readline().strip())
  for nc in xrange(1, N + 1):
    (n, A, B, C, D, x0, y0, M) = [int(x) for x in inf.readline().strip().split()]
    g = gen_grid(n, A, B, C, D, x0, y0, M)
    print "Case #%d: %d" % (nc, count_tri(g))


run(sys.stdin)
