from string import lowercase
from collections import defaultdict

def memoize(f):
    d = {}
    def g(*args):
        if args not in d:
            d[args] = f(*args)
        return d[args]
    return g

def ints():
    return map(int,raw_input().split())

def main():
    N, = ints()
    for case in xrange(N):
        print "Case #%s: %04i" % ((case+1), f(raw_input()))

w = 'welcome to code jam'
def f(s):
    d = defaultdict(set)
    for n,l in enumerate(s):
        if l in w:
            d[l].add(n)

    @memoize
    def ff(nw,ns): # position in w, position in s
        if nw == len(w):
            return 1
        else:
            return sum(ff(nw+1,j+1) for j in d[w[nw]] if j >= ns) % 10000

    return ff(0,0)

if __name__ == '__main__':
    main()
