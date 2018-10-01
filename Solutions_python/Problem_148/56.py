for t in xrange(input()):
    n,x = map(int, raw_input().split())
    a = sorted(map(int, raw_input().split()))
    res = 0
    i = 0
    while i < n-1:
        if a[i] + a[-1] <= x:
            i += 1
        a.pop()
        n -= 1
        res += 1
    if i == n-1:
        res += 1
    print 'Case #%d: %d' % (t+1, res)
