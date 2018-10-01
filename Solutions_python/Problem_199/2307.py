def ret(c, s):
    print 'Case #%d: %s' % (c, s)

def flip(i, s, k):
    for j in xrange(i, i + k):
        s[j] = not s[j]

n = int(raw_input())
for _, c in enumerate(xrange(n)):
    m = raw_input().split(' ')
    s = map(lambda x: x == '+', m[0])
    k = int(m[1])
    q = 0
    for i in xrange(len(s) - k + 1):
        if not s[i]:
            q += 1
            flip(i, s, k)
    if not all(s):
        ret(c + 1, 'IMPOSSIBLE')
    else:
        ret(c + 1, str(q))
