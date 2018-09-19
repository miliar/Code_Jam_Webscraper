#! /usr/bin/env python
import sys
from operator import itemgetter, attrgetter
from sets import Set

# Manage input/output
if len( sys.argv ) < 2:
    print "Usage: program.py [filename]"
    exit( 0 )
filename = sys.argv[1]
fileout = filename.replace( '.in', '.out' )
case = 0
if len( sys.argv ) > 2:
    case = sys.argv[2]

if filename.find( '.in' ) == -1:
    fileout = fileout + '.out'
f = open( filename, 'r' )
fout = open( fileout, 'w' )

vowels = ['a', 'e', 'i', 'o', 'u']

def ValidSubstring( word, anIndex, N ):
    for subIndex in range( anIndex, anIndex + N ):
        if word[subIndex] == 'a' or word[subIndex] == 'e' or word[subIndex] == 'i' or word[subIndex] == 'o' or word[subIndex] == 'u':
            return False
    return True

def GenerateWords( word, anIndex, N ):
    words = Set([])
    for subIndex in range( anIndex+1 ):
        words.add( "0"*(subIndex) + word[subIndex: ] )
    for subIndex in range( anIndex+N, len(word) ):
        for subIndex2 in range( anIndex+1 ):
            words.add( "0"*(subIndex2) + word[subIndex2: subIndex] + "0"*(len(word)-subIndex) )
    return words

def Test( counter ):
    params = f.readline().split()
    word = str( params[0] )
    N = int( params[1] )
    words = Set([])
    for anIndex in range( len(word) - N + 1 ):
        if ValidSubstring( word, anIndex, N ):
            words.update( GenerateWords(word, anIndex, N) )
    print( 'Case #' + str( counter ) + ': '+ str(len(words)) )
    fout.write( 'Case #' + str( counter ) + ': '+ str(len(words)) + '\n' )

# Main
T = int( f.readline() )
    
for counter in range( 1, 1 + T ):
    Test( counter )
    percent = float(counter)/float(T) * 100.0
    print str(percent) + '%'
