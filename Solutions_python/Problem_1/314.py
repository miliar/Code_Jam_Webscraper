#! /usr/bin/env python
import sys
import heapq

class Case(object):
    def __init__(self, engines, queries):
        self.engines = engines
        self.queries = queries

    @staticmethod
    def read(read):
        s = int(read())
        engines = set(read() for i in xrange(s))
        q = int(read())
        queries = [read() for i in xrange(q)]
        return Case(engines, queries)

    def solve(self):
        _E = self.engines
        _Q = self.queries
        if not _Q:
            return 0
        nQ = len(_Q)

        hpush = heapq.heappush
        hpop = heapq.heappop
        pq = []
        best = [nQ] * nQ
        q = _Q[0]
        for e in _E:
            if e != q:
                hpush(pq, (0, 0, e))
        while pq:
            nc, iq, e = hpop(pq)
            if best[iq] < nc:
                continue
            best[iq] = nc
            iq += 1
            if iq == nQ:
                return nc
            q = _Q[iq]
            if e != q:
                hpush(pq, (nc, iq, e))
            else:
                for e2 in _E:
                    if e2 != q:
                        hpush(pq, (nc + 1, iq, e2))

def main():
    read = raw_input
    n = int(read())
    for i in xrange(n):
        c = Case.read(read)
        print 'Case #%d: %d' % (i + 1, c.solve())

if __name__ == '__main__':
    main()
