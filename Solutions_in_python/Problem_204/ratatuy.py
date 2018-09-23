from collections import namedtuple
import sys

Range = namedtuple('Range', 'start end')

def _legal(prov, serv1req, candidate):
    candreq = serv1req * candidate
    return 0.9 * candreq <= prov <= 1.1 * candreq

def divrange(a, b):
    start = a / (1.1 * b)
    end = a / (0.9 * b)
    start = max(int(start) - 10, 0)
    for _ in range(20):
        if _legal(a, b, start):
            break
        start += 1
    else:
        return Range(-9, -10)

    end = int(end) + 10
    for _ in range(20):
        if _legal(a, b, end):
            break
        end -= 1
    else:
        return Range(-9, -10)

    return Range(start, end)

def greedy1(ranges):
    if any(len(r) == 0 for r in ranges):
        return -1
    maxstart = max(r[0].start for r in ranges)
    for r in ranges:
        while r and r[0].end < maxstart:
            del r[0]  # unusable
        if not r:
            return -1
        del r[0]  # The chosen one
    return 1

def count_kits(ranges):
    count = 0
    while True:
        r = greedy1(ranges)
        if r < 0:
            return count
        count += r


if __name__ == "__main__":
    ncases = int(sys.stdin.readline().strip())
    for i in range(ncases):
        N, numpackages = [int(part) for part in sys.stdin.readline().split()]
        required_amounts = [int(part) for part in sys.stdin.readline().split()]
        assert len(required_amounts) == N
        provided = []
        for ning in range(N):
            line = [int(part) for part in sys.stdin.readline().split()]
            assert len(line) == numpackages
            ranges = [divrange(pkg_amount, required_amounts[ning]) for pkg_amount in line]
            ranges = [r for r in ranges if r.start > 0]
            ranges.sort(key=lambda r: r.start)
            provided.append(ranges)

        ## @@
#        print '--------'
#        for l in provided:
#            for r in l:
#                print '%d-%d  ' % (r.start, r.end), 
#            print
#        print '--------'

        sol = count_kits(provided)
        print "Case #%d: %d" % (i+1, sol)
