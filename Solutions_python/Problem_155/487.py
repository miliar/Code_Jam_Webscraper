nc = int(raw_input())
for cid in range(nc):
    s = raw_input().split()
    n, a = int(s[0]), map(int, s[1])
    ans = 0
    for i in range(1, n+1):
        if sum(a[:i]) < i:
            ans = max(ans, i - sum(a[:i]))
    print 'Case #%d: %d' % (cid+1, ans)
