

import sys
from operator import *
from itertools import *
from functools import *
rl = sys.stdin.readline
cases = int( rl() )
to_str = lambda x: '\n'.join( [ ''.join( map( str, y ) ) for y in x ] )
lex_cmp = lambda x, y: ''.join( map( str, x ) ) > ''.join( map( str, y ) )
t = lambda x: map( list, zip( *x ) )
r = lambda x: list( reversed( x ) )
for i in range( 1, cases+1 ):
    print 'Case #%d:'%i,
    cont_flag = False
    n, m = map( int, rl().split() )
    a_ = []
    for i in range( n ):
        a_ += [ map( int, rl().split() ) ]
    s = sorted( set( reduce( add, a_ ) ) )
    del s[0]
    for v in s:
        a, b = map( partial( map, lambda x: 1 if x >= v else 0 ), a_ ), []
        while a != b:
            b = sorted( t( sorted( a ) ) )
            b = sorted( t( sorted( b ) ) )
            a, b = b, a
        b = filter( any, t( filter( any, a ) ) )
        if any( [ len( set(y) ) != 1 for y in b ] ):
            print 'NO'
            cont_flag = True
            break
    if cont_flag:
        continue
    print 'YES'