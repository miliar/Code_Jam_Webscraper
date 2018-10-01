import math

def gcd(a, b):
    while b!=0:
        t=b
        b=a%b
        a=t
    return a

C = int(raw_input())
for c in xrange(C):
    t = map(int, raw_input().split())
    N = t.pop(0)
    g=abs(t[0]-t[-1])
    mint=t[-1]
    for i in xrange(N-1):
        g=gcd(g, abs(t[i+1]-t[i]))
        mint=min(mint, t[i])
    #a=t[0]+g
    m=mint%g
    if (m==0): a=0
    else: a=g-(mint%g)
    print "Case #%d: %d" % (c+1, a), g

