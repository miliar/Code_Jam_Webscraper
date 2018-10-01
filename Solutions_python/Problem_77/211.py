#! /usr/bin/python2

import sys

sys.setrecursionlimit(10000)

def loop_find(field, i, j):
  if (i == j):
    return 1
  else:
    return loop_find(field, field[i], j) + 1

def needed_steps(field, i):
  lf = loop_find(field, field[i], i)
  if lf == 1:
    return 0.0
  else:
    return 1

def main():
  # read in number of test cases
  ntc = int(raw_input())
  for i in range(ntc):
    n = int(raw_input())
    words = raw_input().split(None)
    nums = []
    for j in range(n):
      nums.append(int(words[j])-1)
    # OK, we can start
    steps = 0.0
    for j in range(n):
      steps += needed_steps(nums, j)
    print "Case #{0}: {1}".format(i+1, steps)

if __name__ == '__main__':
  main()
