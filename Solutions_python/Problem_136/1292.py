import sys

f = open(sys.argv[1])

cases = int(f.readline())
for i in xrange(cases):
    S = 0.0
    G = 2.0
    C, F, X = map(float, (f.readline()).split())

    t0 = (X - S) / G
    t1 = (C - S) / G + X / (G + F)

    tmp = 0
    while (t0 > t1):
        t0 = t1
        tmp += (C - S) / G
        G = G + F
        t1 = tmp + (C - S) / G + X / (G + F)

    print "Case #%d:" % (i + 1), t0
