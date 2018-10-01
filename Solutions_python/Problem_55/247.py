from bisect import bisect

class Queue (object):
    def __init__ (self, l):
        self.l = l

        self.cs = [0]
        for x in l:
            self.cs.append(self.cs[-1]+x)

        self.start = 0

        self.memo = [None]*len(self.l)

    def __getitem__ (self, n):
        """Return the number of people in the first n groups."""
        i = (n + self.start) % len(self.cs)
        if i >= self.start:
            return self.cs[i] - self.cs[self.start]
        else:
            return self.cs[i+1] - self.cs[self.start] + self.cs[-1]

    def next (self, k):
        groups = self.memo[self.start]
        if groups is None:
            self.memo[self.start] = groups = bisect(self, k, 0, len(self.cs))-1
        people = self[groups]
        self.start += groups
        self.start %= len(self.l)

        return people

T = int(raw_input())
for case in range(1, T+1):
    R, k, N = map(int, raw_input().split())
    q = Queue(map(int, raw_input().split()))
    euros = 0
    for i in range(R):
        euros += q.next(k)

    print 'Case #%i:' % case, euros
