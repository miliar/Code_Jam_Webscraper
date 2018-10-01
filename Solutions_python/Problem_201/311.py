T = int(raw_input().strip())

for t in range(1, T + 1):
    n, k = map(int, raw_input().split())
    while k > 1:
        n -= 1
        k -= 1
        if k & 1:
            n = n - n / 2
        else:
            n = n / 2
        k = k - k / 2
    print 'Case #%s: %s %s' % (t, n - 1 - (n - 1) / 2, (n - 1) / 2)
