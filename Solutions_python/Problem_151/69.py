
rl = lambda: raw_input().strip()
# f = open('inp')
# rl = lambda: f.readline().strip()

def common_prefix(a, b):
    i = 0
    while i < len(a) and i < len(b) and a[i] == b[i]:
        i += 1
    return i

def count_nodes(words):
    dup = 0
    for a, b in zip(words, words[1:]):
        dup += common_prefix(a, b)
    return sum(map(len, words)) - dup + 1

def go(server, taken, nodes):
    if taken == (2**m)-1: return

    # print 'go(server=%d, taken=%d, nodes=%d)' % (server, taken, nodes)
    global worst, ways
    if server == n-1:
        words = [S[i] for i in xrange(m) if (taken & (2**i)) == 0]
        cand = count_nodes(words) + nodes
        if worst < cand:
            worst = cand
            ways = 1
        elif worst == cand:
            ways += 1
    else:
        remaining = (2**m)-1-taken
        t = remaining
        while t > 0:
            words = [S[i] for i in xrange(m) if (t & (2**i))]
            assert (taken & t) == 0
            go(server+1, taken | t, nodes + count_nodes(words))
            t = (t - 1) & remaining

cases = int(rl())
for cc in xrange(cases):
    print 'Case #%d:' % (cc+1),
    m, n = map(int, rl().split())
    S = [rl() for i in xrange(m)]
    S.sort()

    worst = ways = 0
    go(0, 0, 0)

    # if m <= n:
    #     print '!!!!!!!!!!!!!!!'
    #     print S
    #     print 'n =', n
    print worst, ways % 1000000007
