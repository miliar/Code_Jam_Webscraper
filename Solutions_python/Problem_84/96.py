import sys

def solve(input):
    T = int(input.readline())
    for t in xrange(1, T+1):
        R, C = [int(x) for x in input.readline().split()]
        picture = []
        for _ in xrange(R):
            picture.append([char for char in input.readline().strip()])
        impossible = False
        for r in xrange(R):
            for c in xrange(C):
                if picture[r][c] == '#':
                    if r == R - 1 or c == C - 1:
                        impossible = True
                        break
                    if picture[r][c+1] != '#' or picture[r+1][c] != '#' or picture[r+1][c+1] != '#':
                        impossible = True
                        break
                    picture[r][c] = '/'
                    picture[r][c+1] = "\\"
                    picture[r+1][c] = "\\"
                    picture[r+1][c+1] = '/'
            if impossible:
                break
        
        if impossible:
            print "Case #%d:" % t
            print "Impossible"
        else:
            print "Case #%d:" % t
            for row in picture:
                print ''.join(row)

if __name__ == '__main__':
    solve(sys.stdin)
