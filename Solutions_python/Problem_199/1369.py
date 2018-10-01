#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import stdin

def main():
  n = int(stdin.readline().strip())
  for i in range(n):
    [s, k] = list(stdin.readline().strip().split(' '))
    print("Case #{}: {}".format(i+1, solve(list(s), int(k))))

def solve(s, k):
  n = len(s)
  cnt = 0
  for i in range(n):
    if s[i] == '-':
      if n - i < k:
        return "IMPOSSIBLE"
      cnt += 1
      for j in range(i, i + k):
        s[j] = '-' if s[j] == '+' else '+'
  return cnt

if __name__=="__main__":
  main()
