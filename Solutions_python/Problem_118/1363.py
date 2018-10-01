# -*- coding: utf-8 -*-
import sys
from math import sqrt

def readInts():
  line = sys.stdin.readline().rstrip("\n")
  return map(int,line.split(" "))

def twice(x):
  return x*x

def isPalindrome(x):
  s_x = str(x)
  len_x = len(s_x)
  for i in xrange(len_x/2):
    if s_x[i] != s_x[len_x-1 - i]:
      return False
  return True

if __name__ == "__main__":
  T = readInts()[0]
  palindromes = [1,2,3,4,5,6,7,8,9,11,22,33]
  fairs = []
  for p in palindromes:
    if isPalindrome(p*p):
      fairs.append(p*p)
  for t in xrange(1,T+1):
    A,B = readInts()
    ans = 0
    for e in fairs:
      if A <= e and e <= B:
        ans += 1
    print "Case #%d: %d"%(t,ans)
