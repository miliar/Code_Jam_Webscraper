#!/usr/bin/env python

import sys

case = 0

def is_non_descending(n):
    last = 10 
    while n:
      x=n%10;n=n//10
      if x>last:
          return True
      last = x
    return False

def tidy(n):
    while is_non_descending(n):
        n -= 1    
    print 'Case #'+str(case)+': '+str(n)
sys.stdin.readline()
for line in sys.stdin:
    case += 1
    tidy(int(line))
