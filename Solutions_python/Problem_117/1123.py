#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from sys import stdin, stdout

def main():
  def check():
    for i in xrange(n):
      for j in xrange(m):
        x = lawn[i][j]
        if x < row_m[i] and x < col_m[j]:
          return 'NO'
    return 'YES'

  t = int(stdin.readline())
  for ti in xrange(1, t + 1):
    n, m = [int(s) for s in stdin.readline().strip().split()]
    lawn = [[int(s) for s in stdin.readline().strip().split()] for i in xrange(n)]
    row_m = [max(x) for x in lawn]
    col_m = [max([lawn[j][i] for j in xrange(n)]) for i in xrange(m)]
    print 'Case #%i: %s' % (ti, check())

if __name__ == '__main__':
  main()
