def euclid(a, b):
    if b == 0:
        return a
    return euclid(b, a % b)

for t in range(int(raw_input())):
    n, pd, pg = map(int, raw_input().split())

    d = 100/euclid(pd, 100)

    if d > n or (pg == 100 and pd != 100) or (pg == 0 and pd != 0):
        res = "Broken"
    else:
        res = "Possible"

    print 'Case #%d: %s' % (t+1, res)