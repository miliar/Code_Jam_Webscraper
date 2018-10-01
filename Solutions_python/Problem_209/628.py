def f(i, rem, biggest):
    if (i, rem, biggest) in memo:
        return memo[(i, rem, biggest)]
    if rem == 0:
        return biggest**2
    if i == n:
        return 0
    memo[(i, rem, biggest)] = max(f(i+1, rem-1, max(r[i], biggest)) + 2*r[i]*h[i],
                                  f(i+1, rem, biggest))
    return memo[(i, rem, biggest)]

PI = 3.1415926535898
for tc in xrange(1, int(raw_input())+1):
    n, k = map(int, raw_input().split())
    memo = dict()
    r = []
    h = []
    for _ in xrange(n):
        rr, hh = map(int, raw_input().split())
        r += [rr]
        h += [hh]
    ans = f(0, k, 0) * PI
    print "Case #%d: %.9f" % (tc, ans)

