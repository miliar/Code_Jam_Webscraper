def solve():
    a = map(int, raw_input().split())
    n = a[0]
    a = a[1:]
    d = {}
    for x in a:
        if x in d:
            return [x], d[x]
        for y in d.keys():
            if x + y in d:
                return d[y] + [x], d[x + y]
            d[x + y] = d[y] + [x]
        d[x] = [x]
    return None, None

t = input()
for i in xrange(t):
    a, b = solve()
    print "Case #%d:"%(i+1)
    if a is None:
        print "Impossible"
    else:
        print " ".join(map(str,a))
        print " ".join(map(str,b))
