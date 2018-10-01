
def calc_g(g, k, i):
    # for a group, calc people increment and groups increment
    p, dg = 0, 0
    while p + g[i] <= k:
        p += g[i]
        dg += 1
        i = (i+1) % len(g)
    return p, dg


for t in xrange(int(raw_input())):
    R, k, N = [int(i) for i in raw_input().split()]
    g = [int(i) for i in raw_input().split()]

    if sum(g) <= k:
        euros = R * sum(g)
    else:
        euros = 0

        incr = [None] * N
        for i in xrange(N):
            incr[i] = calc_g(g, k, i)

        r, i = 0, 0
        first = [None] * N
        second = [None] * N

        while r < R:
            if first[i] is None:
                # first time at this group
                # remember rides before this group and people before this group
                first[i] = (r, euros)
            elif second[i] is None:
                # found cycle
                # remember cycle length in rides and people rided
                second[i] = (r - first[i][0], euros - first[i][1])
            
            if second[i] is not None:
                # use cycle
                cr, cp = second[i]
                ncycles = (R - r) / cr
                euros += cp * ncycles
                r += cr * ncycles

            if r < R:
                p, dg = incr[i]
                euros += p
                i = (i + dg) % N
                r += 1

    print "Case #%d: %d" % (t+1, euros)
