#!/bin/env python 
# -*- coding: iso-8859-1 -*-
import os
import sys
import re

def func(l):
  #print l
  base = len(set(l))
  if base == 1:
    base = 2
  n = 2
  m = {}
  zero = False
  for i in range(len(l)):
    q = l[i]
    #print q,
    if i == 0:
      m[q] = 1
    elif not zero and not m.has_key(q):
      m[q] = 0
      zero = True
    elif not m.has_key(q):
      m[q] = n
      n += 1
  #print m
  x = 0
  for i in l:
    x = (x ) * base + m[i]
    #print x
  

  return x

  
def main():
  #f = open('A-test.in')
  #f = open('A-small-attempt1.in')
  f = open('A-large.in')
  n = int(f.readline())

  for i in range(n):
    print 'Case #%s: %s' % (i+1, func(f.readline().strip()))

  
def _test():
  import doctest
  doctest.testmod()


if __name__ == "__main__":
  if len(sys.argv) > 1:
    _test()
  else:
    main()
