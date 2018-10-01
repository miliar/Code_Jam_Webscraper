import sys

def read_string():
    return sys.stdin.readline().strip()

def read_strings():
    return read_string().split()

def read_integer():
    return int( read_string() )

def read_integers():
    return [ int( x ) for x in read_strings() ]

T = read_integer()
for t in range( T ):
    print 'Case #%i:' % ( t + 1 )
    R, C = read_integers()
    board = []
    for r in range( R ):
        board.append( [ c for c in read_string() ] ) 
    possible = True
    for r in range( R ):
        if not possible:
            break
        for c in range( C ):
            if board[ r ][ c ] == '#':
                if r < R - 1 and c < C - 1 and board[ r ][ c + 1 ] == '#' and board[ r + 1 ][ c ] == '#' and board[ r + 1 ][ c + 1 ] == '#':
                    board[ r ][ c ] = '/'
                    board[ r ][ c + 1 ] = '\\'
                    board[ r + 1 ][ c ] = '\\'
                    board[ r + 1 ][ c + 1 ] = '/'
                else:
                    possible = False
                    break
    if possible:
        for row in board:
            print ''.join( row )
    else:
        print 'Impossible'
            
