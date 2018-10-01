from collections import defaultdict
def solve():
    n, k = map(int, raw_input().split())
    d = defaultdict(int)
    d[n] = 1
    while 1:
        nd = defaultdict(int)
        for n in sorted(d.viewkeys(), reverse=True):
            x = (n - 1) / 2
            y = n - 1 - x
            c = d[n]
            k -= c
            if k <= 0:
                print y, x
                return
            if y:
                nd[y] += c
            if x:
                nd[x] += c
        d = nd

T = int(raw_input())
for i in xrange(T):
    print "Case #%d:" % (i + 1),
    solve()
