def n_friends(s_max, s):
    ret = 0
    up = 0
    for i in xrange(s_max + 1):
        if up < i:
            ret += i - up
            up += i - up
        up += s[i]
    return ret

t = int(raw_input())
for k in xrange(1, t+1):
    s_max, s = raw_input().split()
    s_max = int(s_max)
    s = map(int, list(s))
    print 'Case #%d: %d' % (k, n_friends(s_max, s))
