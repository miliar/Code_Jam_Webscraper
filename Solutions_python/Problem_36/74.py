#!/usr/bin/env python

import sys, math
#import fractions
from itertools import repeat, count, cycle, ifilter, ifilterfalse, imap, starmap, tee, izip #, product, combinations, permutations
from collections import defaultdict


def mapInstance( foo, istream ):
  idata = istream.readline()
  return foo( idata )
  
def mapInput( foo, preproc = None, istream = sys.stdin, ostream = sys.stdout ):
  N = map( int, istream.readline().split() )[0]
  odata = starmap( mapInstance, repeat( ( foo, istream ), N ) )
  for i, d in enumerate( odata ):
    print >>ostream, "Case #%d: %s" % ( i+1, d )
  
phrase = "welcome to code jam"
idx = [ [] for i in range(256) ]
for i, c in enumerate( phrase ):
  idx[ ord(c) ].append( i )

def cntWelcome( s ):
  global phrase, idx
  cnt    = [0] * ( len(phrase)+1 )
  cnt[0] = 1

  for c in s:
    for i in idx[ ord(c) ]:
      cnt[i+1] += cnt[i]
  return "%04d" % ( cnt[-1] % 10000 )
      

def main( args ):
  mapInput( cntWelcome )

if __name__ == "__main__":
  main( sys.argv )
