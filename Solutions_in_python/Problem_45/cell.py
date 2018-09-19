import sys, itertools
import bisect

li = sys.stdin.readlines()[1:]

t = 1
for a, b in itertools.izip(li[::2], li[1::2]):
    p, q = map(int, a.split())
    pris = map(int, b.split())
    min = None
    print >> sys.stderr, pris
    for perm in itertools.permutations(pris):
        rel = [0, p+1]
        cost = 0
        for det in perm:
            pos = bisect.bisect_left(rel, det) 
            print >> sys.stderr, pos, rel
            lo, hi = rel[pos-1], rel[pos]
            #(det - lo - 1) + (hi - det - 1)
            cost += hi - lo - 2
            rel.insert(pos, det)
        if not min or cost < min:
            min = cost
    print "Case #%d: %d" % (t, min)
    t += 1
