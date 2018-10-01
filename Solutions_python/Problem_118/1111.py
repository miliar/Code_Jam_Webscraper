#!/usr/bin/env python

import sys
import math

debug = False

if len( sys.argv ) < 2:
  print( "Missing file" )
  sys.exit(1)

def load( fname ):
  with open( fname ) as fd:
    cases = int( fd.readline().strip() )
    for i in range( 1, cases + 1 ):
      minn, maxn = tuple( fd.readline().strip().split() )
      result = solve( int( minn ), int( maxn ) )
      print( "Case #{0}: {1}".format( i, result ) )


def solve( minn, maxn ):
  found = 0
  fair = set()
  for i in range( minn, maxn + 1 ):
    if debug:
      print( "{0}/{1}\r".format( i - minn, maxn+1-minn ) )
    if isFair( i ) and isFair( math.sqrt( i ) ):
      found += 1
  return found

def isFair( num ):
  inum = int( num )
  if inum != num:
    return False
  cn = str( inum )
  l = len( cn )
  for i in range( int( l / 2 ) ):
    if cn[i] != cn[l-i-1]:
      return False
  return True


if __name__ == "__main__":
  load( sys.argv[1] )