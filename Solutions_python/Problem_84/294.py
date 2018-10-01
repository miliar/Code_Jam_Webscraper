import sys

def main():
    f = open(sys.argv[1])
    cases = int(f.readline())
    for i in xrange(1, cases + 1):
        print "Case #%d:" % (i)
        solve(f)
    f.close()

def solve(f):
    rows, cols = map(int, f.readline().split())
    field = []
    outField = [[" "] * cols for i in xrange(rows)]
    for y in xrange(rows):
        field.append(f.readline())
    
    possible = True
    for y in xrange(rows):

        for x in xrange(cols):
            if field[y][x] == "#":
                if outField[y][x] in '\\/':
                    continue
                elif y == rows - 1 or x == cols - 1:
                    print "Impossible"
                    return
                # check field below, to right and below right
                if field[y + 1][x] == '.' or field[y][x+1] == '.' or field[y+1][x+1] == '.' or outField[y+1][x] in "/\\" or outField[y][x+1] in '\\/' or outField[y+1][x+1] in '\\/':
                    print "Impossible"
                    return
                else:
                    outField[y][x] = '/'
                    outField[y+1][x] = '\\'
                    outField[y][x+1] = '\\'
                    outField[y+1][x+1] = '/'
            elif field[y][x] == '.':
                outField[y][x] = '.'
    
    for row in outField:
        print ''.join(row)
main()
