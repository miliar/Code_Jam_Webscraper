for t in range(input()):
    n, s = raw_input().split()
    res = total = 0
    for i, c in enumerate(map(int, s)):
        res += max(0, i-total-res)
        total += c
    print 'Case #%d: %d' % (t+1, res)
