import math

def sel(l, n):
    #print "l, n", l, n
    #print "n", len(l), n
    if n == 0:
        return []
    if n == 1:
        rv = []
        for e in l:
            rv.append([e])
        return rv

    rv = []
    for e in l:
        l2 = list(l)
        l2.remove(e)
        ch = sel(l2, n-1)
        for c in ch:
            c.insert(0, e)
            rv.append(c)
    return rv

def do_case(i):
    N, K = map(int, raw_input().split())
    RH = []
    for j in xrange(N):
        r, h = map(int, raw_input().split())
        RH.append((r,h))

    #print "Case #{}: {}".format(i+1, RH), N, K
    sels = sel(RH, K)

    mv = 0
    for cand in sels:
        hs = sum([2*math.pi*r*h for r,h in cand])
        ba = max(cand, key=lambda x:x[0])
        su = hs + math.pi*ba[0]**2
        if su > mv:
            mv = su
    
    #print "Case #{}: {}".format(i+1, mv), len(sels)
    print "Case #{}: {:.8f}".format(i+1, mv)

def main():
    N = int(raw_input())
    for i in xrange(N):
        do_case(i)

main()

