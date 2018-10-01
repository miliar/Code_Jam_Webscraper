
def memoize(f):
    global memodata
    memodata = {}
    def f2(*args):
        if args not in memodata:
            memodata[args] = f(*args)
        return memodata[args]
    return f2


@memoize
def f(b, k):
    if b >= 2**P:
        # a team
        t = b - 2**P
        if P - k <= M[t]:
            return 0
        else:
            return 2**31
    else:
        b1 = b*2
        b2 = b*2 + 1
        return min(f(b1, k) + f(b2, k),
                   f(b1, k+1) + f(b2, k+1) + cost[b-1])

getnums = lambda: [int(x) for x in raw_input().split()]
T = getnums()[0]
for iter in range(T):
    memodata = {}
    P = getnums()[0]
    M = getnums()
    cost = [-1] * (2**P - 1)
    for i in range(P):
        s = 2**(P-i-1) - 1
        e = 2**(P-i) - 1
        cost[s:e] = getnums()
    print "Case #%d: %d" % (iter+1, f(1,0))
