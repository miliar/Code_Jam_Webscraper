import sys

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

def eventCmp(x, y):
    if x[0] < y[0]:
        return -1
    elif x[0] == y[0]:
        return x[2] - y[2]
    else:
        return 1;
    
def calc(N, fr, to, qty):
    return (long(2)*N + 1 - (to - fr))*(to - fr)/2 * qty
    
# read int
n = int(sys.stdin.readline().strip())
    
for case in range(n):
    # read many ints
    ns = map(int, filter(lambda x: x != '',
                        map(lambda x: x.strip(),
                                sys.stdin.readline().split(' '))))
    N, M = long(ns[0]), long(ns[1])
    events = []
    imcost = long(0)
    for l in range(M):
    # read many ints
        ns = map(int, filter(lambda x: x != '',
                            map(lambda x: x.strip(),
                                    sys.stdin.readline().split(' '))))
        events.append((ns[0], ns[2], 0))
        events.append((ns[1], ns[2], 1))
        imcost = imcost + calc(N, ns[0], ns[1], ns[2])
    events = sorted(events, cmp = eventCmp)    
    # print events
    cost = long(0)
    passangers = []
    for e in events:
        if e[2] == 0:   # enter
            passangers.append((e[0], e[1]))
        else:           # leave
            leave = e[1]
            while leave > 0 and passangers[-1][1] <= leave:
                cost = cost + calc(N, passangers[-1][0], e[0], passangers[-1][1])
                leave = leave - passangers[-1][1]
                passangers.pop() # remove last
            if leave > 0:
                cost = cost + calc(N, passangers[-1][0], e[0], leave)
                p = passangers.pop()
                passangers.append((p[0], p[1] - leave))
                leave = 0
    if len(passangers) != 0:
        print 'F*CK!'
    print 'Case #%d: %s' % (case + 1, (imcost - cost) % 1000002013)