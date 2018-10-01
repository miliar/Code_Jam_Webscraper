from sys import stdin

st = None
filled_board = False
b = None

def read_board():
    b = [stdin.readline().strip() for i in xrange(4)]
    stdin.readline()
    return b

def test_status(line):
    x = line.count('X')
    o = line.count('O')
    t = line.count('T')
    if (x + t == 4): return 'X won'
    if (o + t == 4): return 'O won'
    return None

def solve(b):
    dot = False

    # rows
    for i in xrange(4):
        st = test_status(b[i])
        if (st != None): return st
        if (dot == False): dot = (b[i].find('.') >= 0)
    # columns
    for j in xrange(4):
        st = test_status([b[i][j] for i in xrange(4)])
        if (st != None): return st
    # diagonals
    st = test_status([b[i][i] for i in xrange(4)])
    if (st != None): return st

    st = test_status([b[i][3-i] for i in xrange(4)])
    if (st != None): return st

    if (dot == True):
        return 'Game has not completed'
    else:
        return 'Draw'

if __name__ == '__main__':
    T = int(stdin.readline())
    for caseNum in xrange(T):
        b = read_board()
        st = solve(b)
        print 'Case #%d: %s' % (caseNum + 1, st)
