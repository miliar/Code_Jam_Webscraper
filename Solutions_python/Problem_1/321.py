#!/usr/bin/env python

import sys

import psyco
psyco.full()


class Case:
    def __init__( self, stream ):
        self.engines = {}
        for e in self.__readSection( stream ):
            self.engines[e] = 1

        self.queries = self.__readSection( stream )

    def __readSection( self, stream ):
        N = int( stream.readline() )
        result = []
        for i in range( N ):
            result.append( stream.readline() )
        return result

    def solve( self ):
        switches = 0

        pool = self.engines.copy()

        queries = self.queries
        i = 0
        while i < len( queries ):
            if queries[i] in pool:
                del pool[ queries[i] ]
            i += 1

            if len( pool ) == 1:
                last = pool.keys()[0]
                while i < len( queries ) and queries[i] != last:
                    i += 1
                if i == len( queries ):
                    break
                switches += 1
                pool = self.engines.copy()

        return switches



def log( msg ):
    print >>sys.stderr, msg

def main( args ):
    stream = sys.stdin
    N = int( stream.readline() )
    log( "Number of test cases: %d" % N )
    for i in range( N ):
        c = Case( stream )
        print "Case #%d: %d" % ( i+1, c.solve() )

main( sys.argv )
