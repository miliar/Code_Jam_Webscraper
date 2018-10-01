import heapq as hq
from functools import total_ordering

@total_ordering
class Range(object):
    def __init__(self, l, r):
        self.l = l
        self.r = r
        self.size = r - l + 1
    def __lt__(self, other):
        if self.size != other.size:
            return self.size > other.size
        return self.l < other.l
    def split(self):
        if self.l == self.r:
            return []
        m = (self.l + self.r) / 2
        a = [Range(m+1, self.r)]
        if m-1 >= self.l:
            a.append(Range(self.l, m-1))
        return a
    def sol(self):
        s = self.size - 1
        return s - s/2, s/2
t = int(raw_input())
for kei in xrange(1, t+1):
    n, k = [int(x) for x in raw_input().split(' ')]
    pq = [Range(1, n)]
    ck = 0
    while pq:
        u = hq.heappop(pq)
        ck += 1
        if ck == k:
            break
        for s in u.split():
            hq.heappush(pq, s)
    print "Case #%d: %d %d" % ((kei,) +  u.sol())