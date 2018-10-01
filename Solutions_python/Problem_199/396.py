T = int(raw_input())

def Cool(a):
    l = len(a)
    pos = l - 1
    while pos >= 0 and a[pos] == 1:
        pos -= 1
    return pos

for t in xrange(1, T + 1):
    s, k = raw_input().split()
    a = []
    for i in xrange(len(s)):
        if s[i] == '+':
            a.append(1)
        else:
            a.append(0)
    k = int(k)

    res = 0
    pos = Cool(a)
    while pos != -1:
        if pos < k - 1:
            res = -1
            break
        for i in xrange(pos - k + 1, pos + 1):
            a[i] = 1 - a[i]
        pos = Cool(a)
        res += 1
    if res == -1:
        print "Case #%d: IMPOSSIBLE" % t
    else:
        print "Case #%d: %d" % (t, res)
