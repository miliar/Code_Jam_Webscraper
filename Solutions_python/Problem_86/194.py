#!/usr/bin/python
import sys
import fractions

#f = open( 'input.txt' )
#rl = lambda: f.readline().strip()
rl = lambda: sys.stdin.readline().strip()

gcd = fractions.gcd

def check( values, l, h ):
    for i in range( l, h + 1 ):
        failed = False
        for value in values:
            if i // value * value == i or value // i * i == value:
                continue
            else:
                failed = True
                break
        if not failed:
            return i
    return 0


cases = int( rl() )

for cc in range( cases ):
    
    n, l, h = map( int, rl().split() )
    #print( '{} {} {}'.format( n, pd, pg ))
    
    values = [ val for val in map( int, rl().split() ) ]
    
    result = check( values, l, h )
    if result == 0:
        result = 'NO'
    
    print( "Case #{}: {}".format( cc + 1, result ) )
