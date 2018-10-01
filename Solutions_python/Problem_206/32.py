import sys, itertools, collections
sys.setrecursionlimit(10000)

read_ints = lambda: map(int, raw_input().split())
read_int  = input


for no_t in xrange(1, read_int() + 1):
    d, n = read_ints()
    ks = [read_ints() for _ in xrange(n)]
    ks.sort(key=lambda item: -item[0])
    #print(ks)
    #print([1.0 * (d - k) / s for k, s in ks])
    ans = max([1.0 * (d - k) / s for k, s in ks])
    ans = 1.0 * d / ans
    print 'Case #%d: %s' % (no_t, ans)
