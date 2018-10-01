import sys

memo = {}

def count_larger_recycled(x, B):
    if x not in memo:
        s = str(x)
        valid = set()
        for i in xrange(1, len(s)):
            t = s[i:] + s[:i]
            y = int(t)
            if not t.startswith('0') and x < y:
                valid.add(y)
        memo[x] = valid
    return sum(1 for y in memo[x] if y <= B)

T = int(sys.stdin.readline())
for t, line in enumerate(sys.stdin):
    A, B = [int(tok) for tok in line.split()]
    out = 0
    for i in xrange(A, B+1):
        out += count_larger_recycled(i, B)
    print 'Case #%d: %d' % (t+1, out)
