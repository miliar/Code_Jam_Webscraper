import sys

# read int
n = int(sys.stdin.readline().strip())

def f(t, k):
    t = long(t)
    k = long(k)
    return (2*t + 1)*k + 2*(k-1)*k

def evalUpper(t, p):
    k = long(1)
    while (f(t, k) <= p):
        k = k * 2
    return k

def search(t, p, lim):
    l = long(1)
    r = long(lim)
    while (l < r):
        c = (l + r) / 2
        if f(t, c) > p:
            r = c
        else:
            l = c + 1
    return l - 1
    
for case in range(n):
    # read many ints
    ns = map(int, filter(lambda x: x != '',
                        map(lambda x: x.strip(),
                                sys.stdin.readline().split(' '))))
    t, p = long(ns[0]), long(ns[1])
    lim = evalUpper(t, p)
    result = search(t, p, lim)
    print 'Case #%d: %s' % (case + 1, str(result))