rl = lambda: map(int, raw_input().split())


def solve(p):
    res = 1e200
    for k in xrange(1, max(p) + 1):
        res = min(res, sum(x / k - (0 if x % k else 1) for x in p) + k)
    return res

t = input()
for nt in xrange(t):
    input()
    s = map(int, raw_input().split())
    res = solve(s)
    print "Case #%d:" % (nt + 1), res
