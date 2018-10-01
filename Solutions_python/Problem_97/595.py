
def solve(A, B):
    processed = set()
    smin, smax = str(A), str(B)
    slen = len(smin)
    count = 0
    for n in xrange(A, B + 1):
        s = str(n)
        if s in processed:
            continue
        m = set()
        for t in xrange(slen):
            s = s[-1] + s[:-1]
            if s >= smin and s <= smax and s[0] != '0':
                m.add(s)
        processed.update(m)
        xlen = len(m)
        count += xlen * (xlen - 1)
    return count / 2

def main(f):
    T = int(f.readline())
    for i in xrange(T):
        A, B = map(int, f.readline().split(' '))
        res = solve(A, B)
        print 'Case #%d: %d' % (i + 1, res)

if __name__ == '__main__':
    import sys
    main(sys.stdin)
