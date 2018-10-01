""" Solution to Google Code Jam 2014 Qualification Problem B

Problem statement
=================

Input
-----

Output
------

Limits
------

Doctest
=======

>>> test(
...   testlabel='sample via parse()',
...   testinput='''4
... 30.0 1.0 2.0
... 30.0 2.0 100.0
... 30.50000 3.14159 1999.19990
... 500.0 4.0 2000.0
... ''')  #doctest: +NORMALIZE_WHITESPACE
Case #1: 1.0000000
Case #2: 39.1666667
Case #3: 63.9680013
Case #4: 526.1904762

"""

import sys, os.path
sys.path.insert(0, os.path.abspath('../.lib'));

from codejam import *

def solve(C, F, X):
  T = 0
  P = 2.0
  while True:
    T1 = X / P
    T2 = C / P + X / (P + F)
    if log.debug: log.debug([T, P, T1, T2, C / P, X / (P + F)])
    if T1 > T2:
      T += C / P
      P += F
    else:
      return T + T1

def parse(fi):
  return map(float, fi.next().strip().split())

  return result

def format(r):
  return '%.7f' % r

if __name__ == '__main__':
    main(solve, parse, format)
