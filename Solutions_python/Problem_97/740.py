import sys


class Recycler(object):
    def __init__(self, maxv):
        self.maxv = maxv
        self.R = dict()

    def _calc_recycled(self, n):
        result = set()
        nstr = str(n)
        for i in range(len(nstr)):
            m = int(nstr[i:] + nstr[0:i])
            if n < m and m <= self.maxv:
                result.add(m)
        result = [int(i) for i in result]
        result.sort()
        return result

    def get_recycled(self, n):
        r = self.R.get(n, None)
        if r is None:
            r = self._calc_recycled(n)
            self.R[n] = r
        return r

    def get_recycled_in(self, a, b):
        # R(a,b) = # of recycled pairs (n,m) s.t. a<=n<m<=b
        # Q(a) = # of recycled pairs (n,m) s.t. a<=n<m
        # S(a,b) = # of recycled pairs (n,m) s.t. a<=n<b<=m
        # R(a,b) = Q(a,c)-S(a,b)
        total = 0
        for n in range(a, b):
            r = self.get_recycled(n)
            for m in r:
                if m > b:
                    break
                if n < m:
                    total += 1
        return total


if __name__ == '__main__':
    lines = sys.stdin.readlines()
#    lines = open('test.in', 'r').readlines()
    T = int(lines[0])
    t = 1
    R = Recycler(2000000)
    for line in lines[1:]:
        A, B = line.split()
        A, B = int(A.strip()), int(B.strip())
        print('Case #%d: %d' % (t, R.get_recycled_in(A, B)))
        t += 1


