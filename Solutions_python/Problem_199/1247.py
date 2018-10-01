T = input()
for _ in xrange(T):
    s, n = raw_input().split()
    s = list(s)
    n = int(n)
    ans = 0
    for i in xrange(len(s) - n + 1):
        if s[i] == '+':
            continue
        for j in xrange(i, i + n):
            s[j] = chr(ord('+') + ord('-') - ord(s[j]))
        ans += 1
    s = ''.join(s)
    print 'Case #%d: %s' % (_ + 1, str(ans) if s.count('+') == len(s) else 'IMPOSSIBLE')
