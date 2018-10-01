#!/usr/bin/python2.6
# -*- coding: utf-8 -*-

# AssemblyCompany   = 'Emerging Information Systems Inc.'
# AssemblyTitle     = 'CodeJam2010'
# AssemblyProduct   = 'CodeJam2010'
# AssemblyCopyright = 'Copyright © Emerging Information Systems Inc. 2010'

import sys
import re

output = lambda string: sys.stdout.write( string ) and sys.stdout.flush()

def debug_out( string ):
    if False:
        sys.stderr.write( string )
        sys.stderr.flush()
    pass

def primary_function( riders_str, rkn ):
    """ The Primary function - input a test case as a string, and return the answer string for that test case. """
    debug_out('\n')
    riders = [ int(n) for n in riders_str.split(' ') ]

    inputs = rkn.split(' ')
    runs   = int(inputs[0])
    size   = int(inputs[1])
    length = int(inputs[2])
    assert( length == len(riders) )

    debug_out("runs: %6d,\tsize: %6d,\tlist: %s\n" % ( runs, size, riders ))
    
    weights = {}
    next = {}
    i = 0
    j = 0
    total_money = 0
    while i not in weights.keys() and runs > 0:
        money = 0
        ii = i
        j = 0   # .. I'm not thinking clearly anymore..   coffeeeeeeee...
        while ( money + riders[ii] ) <= size and j < len(riders):
            money += riders[ii]
            ii = ( ii + 1 ) % length
            j += 1
        
        # debug_out('adding index: %d to %d,\tweight: %d\n' % (i, ii, money))
        weights[i] = money
        total_money += money
        runs -= 1
        # roundsize += 1
        # d_roundweight += money
        next[i] = ii
        i = ii
    
    roundmap = {}
    roundsize = 0
    d_roundweight = 0
    while i not in roundmap and runs > 0:
        money = weights[i]
        roundmap[i]    = money
        d_roundweight += money
        total_money   += money
        roundsize += 1
        i = next[i]
        runs -= 1

    debug_out('weights: %s\n' % weights)

    if roundsize > 0 and runs >= roundsize:
        whole_runs = runs / roundsize
        round_money = sum( roundmap.values() )
        assert( round_money == d_roundweight )
        debug_out('whole runs: %4d,\trun_size: %4d,\tround_money: %6d\n' % (whole_runs, roundsize, round_money))

        total_money += round_money * whole_runs
        runs -= roundsize * whole_runs
        
    while runs > 0:
        total_money += weights[i]
        i = next[i]
        runs -= 1

    debug_out('total money: %d\n' % total_money)

    return total_money


class Program:
    def main( self, args ):
        if len(args) < 2:
            print("ERROR: Specify input file...")
            return 1
        else:
            INPUT_FILE = args[1]
            OUTPUT_FILE = re.sub('(.*)[.]in', '\\1.out', INPUT_FILE)

        textReader = open(INPUT_FILE,  'r')
        textWriter = open(OUTPUT_FILE, 'w')

        def output_result( answer ):
            output('Case #%d: %s\n' % (caseNumber, answer))
            textWriter.write('Case #%d: %s\n' % (caseNumber, answer))

        numCases = int( textReader.readline() )  # get the first line
        output("Found %d cases..\n" % numCases)
        
        for caseNumber in xrange( 1, numCases + 1 ):
            rkn_input  = textReader.readline().rstrip('\n')
            list_input = textReader.readline().rstrip('\n')
            output_result( primary_function( list_input, rkn_input ) )
        
        textReader.close()
        textWriter.close()


# Run the program is this file is executed (versus imported)
if __name__ == '__main__':
    import sys
    program = Program()
    sys.exit( program.main( sys.argv ) )
