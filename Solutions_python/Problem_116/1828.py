class E(Exception): pass
def s():
    arr = [ raw_input(), raw_input(), raw_input(), raw_input() ]
    l = [
        [(0, 0), (1, 1), (2, 2), (3, 3)],
        [(0, 3), (1, 2), (2, 1), (3, 0)]
        ]
    for i in xrange(0, 4):
        l.append([(0, i), (1, i), (2, i), (3, i)])
        l.append([(i, 0), (i, 1), (i, 2), (i, 3)])
    was_dot = False
    for i in arr:
        for ch in i:
            if ch == '.': was_dot = True
    for seq in l:
        items = set([ arr[x][y] for x, y in seq ])
        #print items
        _x = items in ({'X'}, {'X', 'T'})
        _o = items in ({'O'}, {'O', 'T'})
        if _x:
            return 'X won'
        elif _o:
            return 'O won'
    if was_dot:
        return 'Game has not completed'
    else:
        return 'Draw'

import sys
for _i in xrange(int(raw_input())):
    print 'Case #%d: %s' % (_i+1, s())
    sys.stdin.readline()
