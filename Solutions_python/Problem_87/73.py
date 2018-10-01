# -*- coding: utf-8 -*-
import sys
fin = sys.stdin
T = int(fin.readline())
for case in range(1,T+1):
    X, S, R, t, N = map(int, fin.readline().split())
    walkways = []
    for i in range(N):
        b, e, w = map(float, fin.readline().split())
        walkways.append((e-b,w))
        X -= e-b
    walkways.append((X,0.0))
    print >> sys.stderr, walkways
    walkways.sort(key=lambda w: w[1])
    print >> sys.stderr, walkways
    time = 0.0
    for l, s in walkways:
        speed = s + R
        runtime = min(t, l/speed)
        t -= runtime
        time += runtime
        remaining = l - runtime*speed
        walktime = remaining / (s+S)
        time += walktime
        
    print "Case #%d: %.7f" % (case, time)

