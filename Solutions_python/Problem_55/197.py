#coding: 1251
#####################################################

from __future__ import division

import os
import sys
import operator
import string
import re
import time


from os.path import splitext
from copy import copy

from math import *
from collections import *
from itertools import *
from functools import *

if len(sys.argv)<=1: 
  sys.argv += [ re.match(r'.*(\w)\w*\.py.*', sys.argv[0]).group(1) + '-tiny.in' ]  

fin, fout = open(sys.argv[1], 'r'), open(splitext(sys.argv[1])[0]+'.out', 'w+')

#####################################################

def solve():
  R, k, N = map(int, next(fin).split())
  gs = map(int, next(fin).split())
  assert len(gs)==N
  
  croud = sum(gs)
  
  groups = cycle(gs)
  def ride(nn, groups):
    board, gs = 0, 0
    for _ in xrange(N):
      if board + nn > k:
        return [board, gs, nn]
      board += nn
      gs += 1

      nn = next(groups)

    return [board, gs, next(groups)]
  
  result, tgs = 0, 0
  nn = next(groups)
  for nr in xrange(R):
    t, gs, nn = ride(nn, groups)
    result += t
    tgs += gs

    if tgs % N == 0: 
      cn, R = divmod(R, nr + 1)
      result *= cn
        
      for nr in xrange(R):
        t, gs, nn = ride(nn, groups)
        result += t      
      break

  
  print>>fout, result

#####################################################

cases = int(next(fin))
start = time.clock()
for case in xrange(cases):  
  print>>sys.stderr, '{0:5}/{1:<5}'.format( case, cases), '\b' * 13,
  print>>fout, 'Case #{0}:'.format( 1+case ),
  solve()

print>>sys.stderr, "[done in: {0:.3f} s]".format(time.clock()-start),

