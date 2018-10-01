def tidy(n):
    s = str(n)
    return s == "".join(sorted(s))

def highest(n):
    if tidy(n): return n
    s = map(int, str(n))
    l = len(s)
    for i in xrange(l - 1, -1, -1):
        if s[i] == 0: continue
        ss = s[:i] + [s[i] - 1] + [9] * (l - i - 1)
        num = reduce(lambda a, b: a * 10 + b, ss)
        if tidy(num):
            return num

T = int(raw_input())
for t in range(T):
    N = int(raw_input())
    print "Case #%d: %d" % (t + 1, highest(N))
