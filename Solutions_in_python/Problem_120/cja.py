import math

T = int(raw_input())

for i in xrange(T):
    r, t = raw_input().split()
    r = int(r)
    t = int(t)

    n = ((1.0 - 2*r) + math.sqrt( (2*r - 1.0)**2 + 8*t ))/4.0
    n = int(n)
    total = (2*r + 1) * n + n*(n-1)*2
    if total <= t:
        print 'Case #%s: %s' % (i+1, n)
    else:
        print 'Case #%s: %s' % (i+1, n-1)
