# Written in python version 3

from decimal import Decimal

def get_cases():
    import sys

    with open( sys.argv[ -1 ], "r" ) as data:
        lines = [ line.rstrip().split() for line in data ]
        lines = lines[ 1 : ]

    cases = [ lines[ index * 3 : index * 3 + 3 ]\
    for index, line in enumerate( lines[ : : 3 ] ) ]

    return cases

def get_result( case ):
    nao = case[ 1 ]
    ken = case[ 2 ]

    def get_win( nao, ken ):
        def process( nao, ken ):
            return len( [ nao[ i ] for i in range( len( nao ) )\
            if nao[ i ] > ken[ i ] ] )

        nao.sort()
        ken.sort()

        mx = process( nao, ken )

        for i in range( len( ken ) ):
            mx = max( mx, process( nao, ken[ i : ] + ken[ : i ] ) )

        return mx

    return str( get_win( nao, ken ) ) + " " +\
    str( int( case[ 0 ][ 0 ] ) - int( get_win( ken, nao ) ) )

cases = get_cases()

for index, case in enumerate( cases ):
    print( "Case #{0}: {1}".format( index + 1, get_result( case ) ) )
