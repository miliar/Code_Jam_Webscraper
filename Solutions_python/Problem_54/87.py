def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a % b)

t = int(raw_input())
tt = 1
while tt <= t:
    v = [long(x) for x in raw_input().split()]
    n = v.pop(0)
    v.sort()
    m = v[1] - v[0]
    for i in range(1, n - 1):
        temp = v[i + 1] - v[i]
        m = gcd(m, temp)
    ans = (m - (v[0] % m)) % m
    print "Case #%d: %d" % (tt, ans)
    tt += 1
