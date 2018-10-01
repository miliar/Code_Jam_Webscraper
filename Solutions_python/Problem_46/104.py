#!/usr/bin/env python

import sys, math
import fractions
from itertools import repeat, count, cycle, ifilter, ifilterfalse, imap, starmap, tee, izip, product, combinations, permutations
from collections import defaultdict
from operator import itemgetter


def mapInstance( foo, istream ):
  N = int( istream.readline() )
  idata = []
  for i in xrange(N):
    idata.append( map( int, istream.readline().strip() )[::-1] )
  return foo( idata )
  
def mapInput( foo, preproc = None, istream = sys.stdin, ostream = sys.stdout ):
  N = map( int, istream.readline().split() )[0]
  if preproc:
    for i in xrange(D):
      preproc( istream.readline().split() )
  odata = starmap( mapInstance, repeat( ( foo, istream ), N ) )
  for i, d in enumerate( odata ):
    print >>sys.stderr, "Case #%d" % ( i+1 )
    print >>ostream, "Case #%d: %s" % ( i+1, d )
  
class showfunction:
  def __init__( self, foo ):
    self.foo = foo
    
  def __call__( self, *args ):
    result = self.foo( *args )
    print >>sys.stderr, args, result
    return result

class cachedfunction:
  def __init__( self, foo ):
    self.foo = foo
    self.cache = {}
    
  def __call__( self, *args ):
    if args in self.cache:
      return self.cache[args]
    else:
      result = self.cache[args] = self.foo( *args )
      return result

def solve( idata ):
  idata = map( lambda x: x+[1], idata )
  rows = map( lambda x: x.index(1), idata )
  
  #@cachedfunction
  def rek(n, visited):
    if n == 0:
      return 0
      
    swap = -1
    mini = 10000
    for i in range(len(rows)):
      if i in visited: continue
      swap += 1
      if rows[i] < n: continue
      this = swap + rek(n-1, visited | set([i]))
      if this < mini:
        mini = this
    return mini
      
  return str( rek(len(rows)-1, set()) )
  
def main( args ):
  mapInput( solve )

if __name__ == "__main__":
  main( sys.argv )
