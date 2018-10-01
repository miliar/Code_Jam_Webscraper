#!/usr/bin/env python

T = [[(x,x) for x in xrange(4)],[(x,3-x) for x in xrange(4)]] + [[(x,y) for x in xrange(4)] for y in xrange(4)] + [[(y,x) for x in xrange(4)] for y in xrange(4)]
z = int(raw_input())
for case in xrange(1,z+1):
    print "Case #" + str(case) + ":",
    l = [list(raw_input()) for i in xrange(4)]
    raw_input()
    for t in T:
        if all([l[i][j] == 'X' or l[i][j] == 'T' for i,j in t]):
            print "X won"
            break
        elif all([l[i][j] == 'O' or l[i][j] == 'T' for i,j in t]):
            print "O won"
            break
    else:
        if all([l[i][j] != '.' for i in xrange(4) for j in xrange(4)]):
            print "Draw"
        else:
            print "Game has not completed"