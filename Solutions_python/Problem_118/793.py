#!/usr/bin/env python

from math import sqrt

T = int(raw_input())

def read_problem():
  a, b = [int(i) for i in raw_input().split()]
  return a, b

def is_palindrome(s):
  for idx in range(len(s)/2):
    if s[idx] != s[-1*(idx+1)]:
      return False
  return True

def solve(problem):
  a, b = problem
  i = int(sqrt(a))
  if i*i != a:
    i += 1
  count = 0
  while i*i <= b:
    if is_palindrome(str(i*i)) and is_palindrome(str(i)):
      count += 1
    i += 1
  return count

for n in range(T):
  problem = read_problem()
  solution = solve(problem)
  print 'Case #%d: %s' %(n+1, solution)

