#! /usr/bin/env python
import sys
from operator import itemgetter, attrgetter

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

# 0  1  2  3
# 4  5  6  7
# 8  9 10 11
#12 13 14 15
solutions = [ [0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15], [0, 4, 8, 12], [1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [0, 5, 10, 15], [12, 9, 6, 3]]

def TestSolution( board, solution, symbol ):
    for anIndex in solution:
        if board[anIndex] != 'T' and board[anIndex] != symbol:
            return False
    return True

def Test( counter ):
    board = f.readline().replace('\n', '')
    board += f.readline().replace('\n', '')
    board += f.readline().replace('\n', '')
    board += f.readline().replace('\n', '')
    emptyLine = f.readline()

    xwin = False
    ywin = False
    for solution in solutions:
        xwin |= TestSolution( board, solution, 'X' )
        ywin |= TestSolution( board, solution, 'O' )

    result = "Game has not completed"
    if xwin:
        result = "X won"
    elif ywin:
        result = "O won"
    elif board.find('.') == -1:
        result = "Draw"
#"X won"
#"O won"
#"Draw"
#"Game has not completed"    
    
    fout.write( 'Case #' + str( counter ) + ': '+ str(result) + '\n' )

# Main
T = int( f.readline() )
    
for counter in range( 1, 1 + T ):
    Test( counter )
    percent = float(counter)/float(T) * 100.0
    print str(percent) + '%'
