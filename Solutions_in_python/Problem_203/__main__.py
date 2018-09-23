import numpy as np

def solve():
    R,C = map(int,raw_input().split())
    cake = np.zeros((R,C), dtype='str')

    for r in xrange(R):
        cake[r] = list(raw_input())

    for r in xrange(R):
        last = '?'
        for c in xrange(C):
            if cake[r][c] == '?':
                cake[r][c] = last
            else:
                last = cake[r][c]
        last = '?'
        for c in xrange(C-1,-1,-1):
            if cake[r][c] == '?':
                cake[r][c] = last
            else:
                last = cake[r][c]


    for c in xrange(C):
        last = '?'
        for r in xrange(R):
            if cake[r][c] == '?':
                cake[r][c] = last
            else:
                last = cake[r][c]
        last = '?'
        for r in xrange(R-1,-1,-1):
            if cake[r][c] == '?':
                cake[r][c] = last
            else:
                last = cake[r][c]

    res = ''
    for row in cake[:]:
        res += ''.join(row)
        res += '\n'
    return res.strip()

T = int(raw_input())
for tt in xrange(T):
    print 'Case #{}:'.format(tt+1)
    print solve()
