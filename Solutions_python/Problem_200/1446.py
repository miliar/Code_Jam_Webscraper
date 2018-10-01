#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import stdin

def main():
  n = int(stdin.readline().strip())
  for i in range(n):
    k = stdin.readline().strip()
    print("Case #{}: {}".format(i+1, solve(k).lstrip("0")))

def is_tidy(k):
  return "".join(list(sorted(k))) == k

def monotonicity_change(k):
  curr = '0'
  for c in k:
    if curr > c:
      return str(int(curr) - 1)
    curr = c

def solve(k):
  n = len(k)
  if is_tidy(k):
    return k
  x = monotonicity_change(k)
  s = ""
  for i in range(n):
    if k[i] > x:
      return s + x + "9" * (n - i -1)
    s += k[i]
  return s

if __name__=="__main__":
  main()
