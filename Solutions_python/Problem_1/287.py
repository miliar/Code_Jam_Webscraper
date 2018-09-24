#!/usr/bin/env python

#---------------------------------------------------------------------------
# Google Code Jam 2008
#
# Gavin Baker <gavinb@antonym.org>
#
# Qualification Round
# A: Saving the Universe
#---------------------------------------------------------------------------

import sys
from collections import defaultdict

def next_best_engine(cur_engine, engines, queries):
    '''
    Returns the next best engine, excluding the named engine, to process
    the queries.

    Chooses the engine that will give the longest run for the query list.
    '''

    #print '; cur=', cur_engine, 'queries=', queries

    # The next position, or past the end for engines not in query
    next_pos = dict([(e, len(queries)+1) for e in engines if e != cur_engine])

    # Find run lengths
    for e in engines:
        if e != cur_engine:
            # Get the first position of this engine in queries
            for i, q in enumerate(queries):
                if q == e:
                    next_pos[q] = i
                    break

    #print '; next_pos: ', next_pos

    # Return longest run
    ef = [(next_pos[e], e) for e in next_pos]
    ef.sort()
    ef.reverse()
    #print '; next_pos sorted: ', ef
    return ef[0][1]

def solve(infile):

    engines = []
    queries = []

    # Read S Engines
    S = int(infile.readline())
    for i in range(0, S):
        engine = infile.readline().strip()
        #print '; Engine #%u: %s' % (i, engine)
        engines.append(engine)

    # Read Q Queries
    Q = int(infile.readline())
    for i in range(0, Q):
        query = infile.readline().strip()
        #print '; Query #%u: %s' % (i, query)
        queries.append(query)

    # Process queries

    cur_engine = next_best_engine(None, engines, queries)
    switches = 0
    #print '; Starting engine ', cur_engine

    for i, query in enumerate(queries):
        #print '; process', i, ': e = ', cur_engine, '\tq = ', query
        if query == cur_engine:
            switches += 1
            # Choose the next best engine
            cur_engine = next_best_engine(cur_engine, engines, queries[i:])
            #print '; switch ', switches, 'to', cur_engine

    return switches

def process(infile):

    N = int(infile.readline())

    for case_num in range(0, N):
        result = solve(infile)
        print 'Case #%u: %u' % (case_num+1, result)

if __name__=='__main__':
    process(sys.stdin)
