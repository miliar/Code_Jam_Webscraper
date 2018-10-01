#!/usr/bin/env python3

import sys

if "__main__" == __name__:

    readline = sys.stdin.readline

    cases_count = int( readline( ) )

    for case_number in range( 1, cases_count + 1 ):

        rate = 2.0
        factory_cost, extra_rate, goal = map( float, readline( ).split( ) )

        time_elapsed = 0.0
        old_time_to_goal = goal / rate
        time_to_goal = 0.0
        while True:

            time_elapsed += factory_cost / rate
            rate += extra_rate
            time_to_goal = time_elapsed + goal / rate
            
            if not time_to_goal < old_time_to_goal:
                break

            old_time_to_goal = time_to_goal

        print( "Case #{0}: {1:.7f}".format( case_number, old_time_to_goal ) )

# vim: set syntax=python ts=4 sts=4 sw=4 et tw=79:
