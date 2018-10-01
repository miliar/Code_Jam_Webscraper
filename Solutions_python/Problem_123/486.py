"""Osmos"""

'''
Notes
* Always add max possible, i.e. A-1
'''

import sys
from math import ceil, log
import numpy as np

#import decimal
'''
decimal.getcontext().prec = 60
zero = decimal.Decimal(0)
one = decimal.Decimal(1.0)
two = decimal.Decimal(2.0)
four = decimal.Decimal(4.0)
'''

debug = False

def solve(A, M, depth=0):
  if debug: print "solve(): {}>> A = {}, M = {}".format("| " * depth, A, M)
  N = len(M)
  if N == 0:
    if debug: print "solve(): {}<< 0 [Case: N == 0]".format("| " * depth)
    return 0
  elif N == 1:
    if M[0] < A:
      if debug: print "solve(): {}<< 0 [Case: N == 1, M[0] < A]".format("| " * depth)
      return 0
    else:
      if debug: print "solve(): {}<< 1 [Case: N == 1, M[0] >= A]".format("| " * depth)
      return 1  # either add one mote or remove this bigger mote
  else:  # N > 1
    if M[0] < A:
      if debug: print "solve(): {}** Eat M[0] = {} [Case: N > 1, M[0] < A]".format("| " * depth, M[0])
      steps = solve(A + M[0], M[1:], depth + 1)
      if debug: print "solve(): {}<< {} [Case: N > 1, M[0] < A]".format("| " * depth, steps)
      return steps
    else:
      if A == 1:
        if debug: print "solve(): {}<< {} [Case: N > 1, M[0] >= A, A == 1]".format("| " * depth, N)
        return N  # cannot consume any, remove all
      
      d = (M[0] + 1) - A
      if d < A:
        if debug: print "solve(): {}** Add 1 mote with size (A - 1) = {} and eat it to reach size = {}, Eat M[0] = {} [Case: N > 1, M[0] >= A, A > 1]".format("| " * depth, A - 1, A + (A - 1), M[0])
        steps = 1 + solve(A + (A - 1) + M[0], M[1:], depth + 1)  # add new mote with max possible size (A - 1), eat M[0], and move on
        if debug: print "solve(): {}<< {} [Case: N > 1, M[0] >= A, A > 1]".format("| " * depth, steps)
        return steps
      else:
        #return 1 + solve(A, M[1:], depth + 1)  # always remove mote M[0] NOTE: doesn't work if it's bad choice for future
        
        if debug: print "solve(): {}*1 Remove M[0] = {} [Case: N > 1, M[0] >= A, A > 1]".format("| " * depth, M[0])
        steps1 = 1 + solve(A, M[1:], depth + 1)  # option 1: remove M[0]
        
        k = int(ceil(log(float(M[0]) / float(A - 1), 2)))   # M[0] + 1 - 1 = M[0]  #int(ceil(log(float(M[0] - 1) / float(A - 1), 2)))
        if debug: print "solve(): {}*2 Add k = {} motes to reach total size = {}, Eat M[0] = {} [Case: N > 1, M[0] >= A, A > 1]".format("| " * depth, k, (2**k * (A - 1) + 1), M[0])
        steps2 = k + solve((2**k * (A - 1) + 1) + M[0], M[1:], depth + 1)  # option 2: add what is needed to eat M[0], and move on (maybe this will be a better choice later)
        
        steps = min(steps1, steps2)
        if debug: print "solve(): {}<< {} = min({}, {}) [Case: N > 1, M[0] >= A, A > 1]".format("| " * depth, steps, steps1, steps2)
        return steps

def osmos():
  T = int(raw_input())
  for case in range(T):
    if debug: print "\nosmos(): Case #{}".format(case + 1)
    
    A, N = tuple(int(x) for x in raw_input().split())
    if debug: print "osmos(): A = {}, N = {}".format(A, N)
    
    M = [int(x) for x in raw_input().split()]
    if debug: print "osmos(): M = {}".format(M)
    
    M.sort()
    if debug: print "osmos(): sorted M = {}".format(M)
    
    steps = solve(A, M)
    
    print "Case #{}: {}".format(case + 1, steps)

if __name__ == "__main__":
  debug = '--debug' in sys.argv
  osmos()
