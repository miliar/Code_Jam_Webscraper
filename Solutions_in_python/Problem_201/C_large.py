T = int(raw_input())

def GetValue(x):
    return (x / 2, (x - 1) / 2)

for t in xrange(1, T + 1):
    n, k = map(int, raw_input().split())
    v = 1
    while True:
        if v * 2 <= k:
            v *= 2
        else:
            break
    w = k - v
    left = n - v + 1
    p = left / v
    q = left % v
    if w < q:
        p += 1
    max_v, min_v = GetValue(p)
    print "Case #%d: %d %d" % (t, max_v, min_v)
