from sys import argv
from itertools import izip, imap, count, combinations, permutations
import math

def direction( v, w, s, mind ):
    r = [ s + i for i in w ]
    diff = [ abs(i-j) for i, j in izip(v, r) ]
    d0 = max(diff)
    r = [ s + 0.000001 + i for i in w ]
    diff = [ abs(i-j) for i, j in izip(v, r) ]
    d1 = max(diff)
    
    #if (abs(d1-d0) /  )<:
    #    return 0, d0
    if d0 < 0.0000005:
        return 0, 0
    if d1 > d0 :
        return 1, d0
    if d1 < d0 :
        return -1, d0
    return 0, d0

def solvecase( D, v ):
    #global inf
    v.sort()
    s = v[0]
    v = [ float(i-s) for i in v ]
    l = len(v)
    #dp[0] = 0
    #dp[1] = if v[1]-v[0]>D --> dp[0]
    #naive:
    w = [ v[0] ]
    for i in v[1:]:
        w.append( max( i, D+w[-1] ) )
    
    mind = 0.0000005  * D
    step = float( -(l-1)*D )
    s = 0.0
    while True:
        d, t = direction( v, w, s, mind )#/2.1 )
        #print [ s + i for i in w ]
        #print d
        #print t
        if d == -1: # go left
            #print s, "-"
            s -= step
        elif d == 1: # go right
            #print s, "+"
            s += step
        step /= 2
        #print step, mind
        if abs(step) < mind:
            break
    #print [ s + i for i in w ]
    return t

def main():
    global inf
    inf = argv[1]
    inf = open(argv[1])
    ncase = int(inf.readline().strip())
    for case in xrange(1, ncase+1):
        CD = inf.readline().strip()
        C, D = map(int, CD.split())
        v = []
        for i in xrange(C):
            PV = inf.readline().strip()
            P, V = map(int, PV.split())
            v.extend( [P]*V )
        ans = solvecase( D, v )
        print "Case #{n}: {a}".format( n=case, a = ans )

main()

