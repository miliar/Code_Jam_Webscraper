

import sys

def gcd(a, b):
    if 0 == b:
        return a
    return gcd(b, a % b)

C = int(sys.stdin.readline())
for case in range(C):
    line = sys.stdin.readline()
    tokens = line.split()
    N = int(tokens[0])

    ts = map(int, tokens[1:])

    #print "C", C, "N", N, "ts", ts

    g = None
    for a in range(N):
        for b in range(a+1, N):
            diff = abs(ts[b] - ts[a])
            if None == g:
                g = diff
            else:
                g = gcd(g, diff)

    phase = ts[0] % g
    print "Case #%d:" % (case+1), (g - phase) % g

