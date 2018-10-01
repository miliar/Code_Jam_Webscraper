#!/bin/python
#
# Alien Language
# Runs with Python 2.5.2
#
# Run this program with the path to the input file as its only parameter.
import sys, re

if len( sys.argv ) < 2:
    print "Where's my datafile?"
    exit(1)
    
fp = open( sys.argv[1], 'rb' )

L, D, N = map( int, fp.readline().split() )

words = []
for i in xrange( D ):
    words.append( fp.readline() )

for i in xrange( N ):
    # Create a compiled regular expression
    pattern = re.compile( '^' + fp.readline()
        .replace( '(', '[' )
        .replace( ')', ']' ) + '$' )
    
    # Execute it on the dictionary and count the matches
    matches = 0
    for word in words:
        if pattern.match( word ):
            matches += 1

    print "Case #%d: %d" % ( i + 1, matches )