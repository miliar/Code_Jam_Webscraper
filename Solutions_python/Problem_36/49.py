import sys

def readline():
    return sys.stdin.readline().strip()

search = 'welcome to code jam'

for n in range( int( readline() ) ):
    line = readline()
    lookup = [ [ 0 for line_letter in line ] for search_letter in search ]
    for search_index, search_letter in enumerate( search ):
        letter_count = 0
        total = 0
        for line_index, line_letter in enumerate( line ):
            if line_letter == search_letter:
                if search_index == 0:
                    total += 1
                else:
                    total = total + lookup[ search_index - 1 ][ line_index ]
            lookup[ search_index ][ line_index ] = total
    print 'Case #%i: %04i' % ( n + 1, lookup[ -1 ][ -1 ] % 10000 )
