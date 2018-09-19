#!/usr/bin/python

def doit():
    n, k = map(int, raw_input().split())

    def rotate(a):
        r = []
        for x in xrange(n):
            s = []
            for y in xrange(n):
                s.append(a[n-1-y][x])
            r.append(s)
        #prt(r)
        return r

    def gravity(a):
        for x in xrange(n):
            i = n-1
            for y in xrange(n):
                t = a[n-1-y][x]
                if t == '.':
                    continue
                a[i][x] = t
                i -= 1
            while i >= 0:
                a[i][x] = '.'
                i -= 1
        #prt(a)
        return a

    def get(a, x, y, d):
        dir = [(0,1),(1,0),(1,1),(1,-1)]
        s = ''
        for i in xrange(k):
            s += a[x][y]
            x += dir[d][0]
            y += dir[d][1]
            if x < 0 or y < 0 or x >= n or y >= n: break
        return s

    def win(a, c):
        dst = c * k
        for x in xrange(n):
            for y in xrange(n):
                for i in xrange(4):
                    if get(a, x, y, i) == dst: return True
        return False

    board = []
    for x in xrange(n):
        board.append(list(raw_input().strip()))

    def prt(a):
        print ''
        for x in xrange(n):
            s = ''
            for y in xrange(n):
                s += a[x][y]
            print s

    #prt(board)
    board = gravity(rotate(board))
    r = win(board, 'R')
    b = win(board, 'B') 
    if r and b:
        return 'Both'
    if r:
        return 'Red'
    if b:
        return 'Blue'
    return 'Neither'

t=input()
for x in xrange(t):
    print 'Case #%d: %s' % (x+1, doit())
