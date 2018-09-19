#!/usr/bin/python

def solve(lowest, highest, numbers):
  # find a number lowest < n < highest such that
  # foreach a in numbers:
  #   either a % n == 0
  #   or n % a == 0
  for i in xrange(lowest, highest + 1):
    if all([ i % a == 0 or a % i == 0 for a in numbers]):
      return i
  return None
  
if __name__ == "__main__":
  print solve(2, 100, [3, 5, 7])
  print solve(8, 16, [1, 20, 5, 2])
