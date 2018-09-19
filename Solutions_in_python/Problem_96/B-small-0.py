h = [0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]
hs = [0, 0, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 0, 0]

import itertools
import sys
readline = sys.stdin.readline

t = int( readline() )
for i in range( t ):
    numbers = tuple( map( int, readline().split( ' ' ) ) )
    n, s, p = numbers[ :3 ]
    t = numbers[ 3: ]
    m = 0
    if s:
        for c in itertools.combinations( range( n ), s ):
            c = set( c )
            r = 0
            for j in range( n ):
                if p <= ( hs if j in c else h )[ t[ j ] ]:
                    r += 1
            m = max( m, r )
    else:
        for j in range( n ):
            if p <= h[ t[ j ] ]:
                m += 1
    print( 'Case #{}: {}'.format( i + 1, m ) )
