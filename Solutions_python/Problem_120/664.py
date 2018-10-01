#!/usr/bin/env python

import sys
import time
import logging

if len( sys.argv ) < 2:
  print( "Missing file" )
  sys.exit(1)

log = logging.getLogger( __name__ )
log.addHandler( logging.StreamHandler() )
if '-d' in sys.argv:
  log.setLevel( logging.DEBUG )
else:
  log.setLevel( logging.CRITICAL )


def load( fname ):
  with open( fname ) as fd:
    cases = int( fd.readline().strip() )
    for i in range( 1, cases + 1 ):
      log.debug( "Doing case #{0}".format( i ) )
      whiter, paintu = tuple( fd.readline().strip().split() )
      result = solve( int( whiter ),  int( paintu ) )
      print( "Case #{0}: {1}".format( i, result ) )

def solve( whiter, paintu ):
  circles = 0
  while True:
    usep = whiter*2 + 1
    if paintu - usep >= 0:
      paintu -= usep
      circles += 1
      whiter += 2
    else:
      return circles



if __name__ == "__main__":
  load( sys.argv[1] )