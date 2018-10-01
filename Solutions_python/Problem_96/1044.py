def solve(xs):
    n, s, p = xs[:3]
    ts = xs[3:]
    assert len(ts) == n
    result = sum(1 for t in ts if t >= 3*p - 2)
    improveable = set([3*p-3, 3*p-4]) - set([0,1,29,30])
    poss = sum(1 for t in ts if t in improveable)
    result += min(s, poss)
    return result


import sys
def main():
    L = list(sys.stdin)
    for t in range(1,1+int(L[0])):
        print 'Case #%d: %d' % (t, solve(map(int, L[t].split())))

main()
