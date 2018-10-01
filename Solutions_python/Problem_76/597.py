from itertools import combinations

cases = raw_input()
for case in xrange(int(cases)):
    n = int(raw_input())
    c = [int(i) for i in raw_input().strip().split()]

    smax = 0
    for i in xrange(1, n):
        for j in combinations(c, i):
            p = 0
            s = 0
            ssum = 0
            temp = list(c)
            for k in j:
                p ^= k
                temp.remove(k)
            for l in temp:
                s ^= l
                ssum += l
            if p == s and ssum > smax:
                smax = ssum

    if smax == 0:
        smax = 'NO'
    print 'Case #%d: %s' % (case + 1, smax)
