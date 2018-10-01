#!/usr/bin/env python
import fileinput
import gmpy

def is_palindrome(s):
  slen = len(s)
  for i in xrange(slen/2):
    if s[i] != s[slen-1-i]:
      return False
  return True

def find_fairsquare(A, B, caseNum):
  num = 0
  for x in xrange(A, B+1):
    if is_palindrome(str(x)):
      (a,b) = gmpy.sqrtrem(x)
      if b == 0 and is_palindrome(str(a)):
        num += 1
  print "Case #%d: %d" % (caseNum, num)

def main():
  caseNum = 1
  for line in fileinput.input():
    L = line.split()
    if (len(L) == 1):
      continue
    find_fairsquare(int(L[0]), int(L[1]), caseNum)
    caseNum += 1

if __name__ == '__main__':
  main()
