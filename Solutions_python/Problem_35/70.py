#!/usr/bin/env python

import sys, math
#import fractions
from itertools import repeat, count, cycle, ifilter, ifilterfalse, imap, starmap, tee, izip #, product, combinations, permutations
from collections import defaultdict


def mapInstance( foo, istream ):
  H, W = map( int, istream.readline().split() )
  idata = [ map( int, istream.readline().split() ) for i in range( H ) ]
  return foo( idata, H, W )
  
def mapInput( foo, preproc = None, istream = sys.stdin, ostream = sys.stdout ):
  N = map( int, istream.readline().split() )[0]
  odata = starmap( mapInstance, repeat( ( foo, istream ), N ) )
  for i, d in enumerate( odata ):
    print >>sys.stderr, "Case #%d" % ( i+1 )
    print >>ostream, "Case #%d:\n%s" % ( i+1, d )
  
def water( alt, h, w ):
  labels = [ [None]*w for i in range(h) ]

  def getlabel( y, x, basin ):
    if labels[y][x]: # already labelled?
      return labels[y][x]
    directions = [ (y-1,x), (y,x-1), (y,x+1), (y+1,x) ]
    min        = 1000000
    argmin     = None
    for ny,nx in directions:
      if ny >= 0 and nx >= 0 and ny < h and nx < w:
        if alt[ny][nx] < alt[y][x] and alt[ny][nx] < min:
          min    = alt[ny][nx]
          argmin = (ny,nx)
    if argmin: # no sink?
      basin = getlabel( argmin[0], argmin[1], basin )
    labels[y][x] = basin
    return basin

  basins = [ chr( ord('a')+i ) for i in xrange(26) ]
  i = 0
  for y in xrange( h ):
    for x in xrange( w ):
      if not labels[y][x]:
        label = getlabel( y, x, basins[i] )
        #print '\n'.join( map( ' '.join, map(str,labels) ) )
        if label == basins[i]: # label used
          i += 1

  return '\n'.join( map( ' '.join, labels ) )


def main( args ):
  mapInput( water )

if __name__ == "__main__":
  #try:
  #  import psyco
  #  psyco.full()
  #except Exception, e:
  #  print "psyco not found"
  main( sys.argv )
