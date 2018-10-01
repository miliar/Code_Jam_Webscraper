# Written in python version 3

from decimal import Decimal

def get_cases():
    import sys

    with open( sys.argv[ -1 ], "r" ) as data:
        lines = [ line.rstrip().split() for line in data ]

    return lines[ 1 : ]

def get_result( case ):
    C, F, X = list( map( Decimal, case ) )

    used_time = 0
    current_production = 2

    expected_time = 1
    future_expected_time = 0

    while ( expected_time > future_expected_time ):
        expected_time = used_time + X / current_production

        future_expected_time = used_time + C / current_production +\
        X / ( current_production + F )

        used_time += C / current_production
        current_production += F

    return expected_time

cases = get_cases()

for index, case in enumerate( cases ):
    print( "Case #{0}: {1}".format( index + 1,\
    round( get_result( case ), 7 ) ) )
