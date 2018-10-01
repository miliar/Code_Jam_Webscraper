import sys

t = int(raw_input())
for case in xrange(t):
    n, k = map(int, raw_input().split())
    segs = [n]
    next_segs = []
    soln = (0,0)

    for _ in xrange(k):
        if not segs:
            segs, next_segs = next_segs, []
            segs.sort()
        seglen = segs.pop()
        next_segs.append((seglen - 1) / 2)
        next_segs.append(seglen / 2)
        soln = (seglen / 2, (seglen - 1) / 2)

    print 'Case #%d: %s' % (case+1, ' '.join(map(str, soln)))
    sys.stdout.flush()
