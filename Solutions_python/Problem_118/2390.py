import sys
f = sys.stdin
o = sys.stdout
T = int(f.readline().strip())


def solve():
    import math
    for t in xrange(T):
        c = 0
        m, n = [int(n) ** 0.5 for n in f.readline().strip().split(' ')]
        m, n = int(math.ceil(m)), int(n)
        for i in range(m, n + 1):
            if r(i) and r(i ** 2):
                c += 1
        s = "Case #%d: %s\n" % (t + 1, c)
        o.write(s)


def r(n):
    s = str(n)
    return s == ''.join(reversed(s))
solve()
