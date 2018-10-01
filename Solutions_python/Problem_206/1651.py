#!/usr/bin/env python3

import sys
from operator import itemgetter

def main():
  fi = sys.stdin
  fo = sys.stdout
  case_count = int(fi.readline().strip())
  for i in range(1, case_count+1):
    d, n, ks, ss = read_input(fi)
    solution = solve(d, n, ks, ss)
    display_and_clear(fo, i, solution)

def read_input(f):
  d, n = [int(arg) for arg in f.readline().split()]
  ks = []
  ss = []
  for i in range(n):
    k, s = [int(arg) for arg in f.readline().split()]
    ks.append(k)
    ss.append(s)

  return d, n, ks, ss

def display_and_clear(f, i, solution):
  f.write('Case #%d: %.6f\n' % (i, solution))
  f.flush()

def solve(d, n, ks, ss):
  ks.append(d)
  ss.append(1)

  kis = [(k, i) for i, k in enumerate(ks)]
  kis = sorted(kis, key=itemgetter(0), reverse=True)

  min_time = float('inf')
  for i in range(n):
    k1, hi1 = kis[i]
    k2, hi2 = kis[i + 1]

    d1 = d - k1
    t1 = d1 / ss[hi1]

    d2 = d - k2
    t2 = d2 / ss[hi2]

    if ss[hi2] > ss[hi1]:
      between = k1 - k2
      catch_time = between / (ss[hi2] - ss[hi1])
    else:
      catch_time = float('inf')
    #print('----')
    #print('k1: %s, d1: %s, h1: %s' %(k1, d1, ss[hi1])) 
    #print('k2: %s, d2: %s, h2: %s' %(k2, d2, ss[hi2]))
    #print('between: %s' % between)
    #print('catch_time: %s' % catch_time)
    if catch_time > 0 and catch_time < t1:
      dist_remain = d2 - ss[hi2] * catch_time
      min_time = catch_time + dist_remain / ss[hi1]
    else:
      min_time = t2

    #print('min_time: %s' % min_time)

  return d / min_time

if __name__ == '__main__':
  main()

