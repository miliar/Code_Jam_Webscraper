# Written in Python 3

def get_cases():
    import sys

    with open( sys.argv[ -1 ], "r" ) as data:
        lines = [ line.rstrip().split() for line in data ]

    return lines[ 1 : ]

def get_result( case ):
    A, B, K = list( map( int, case ) )

    result = 0

    for i in range( A ):
        for j in range( B ):
            if i & j < K:
                result += 1

    return result

cases = get_cases()

for index, case in enumerate( cases ):
    print( "Case #{0}: {1}".format( index + 1, get_result( case ) ) )
