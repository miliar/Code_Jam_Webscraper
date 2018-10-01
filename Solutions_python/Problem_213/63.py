import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()


def main():
    tt = I()
    rr = []
    for ti in range(1,tt+1):
        n,c,m = LI()
        d = collections.defaultdict(int)
        e = [0] * n
        for _ in range(m):
            a,b = LI_()
            d[b] += 1
            e[a] += 1

        r = max(d.values())
        em = 0
        for i in range(n):
            em += e[i]
            if (em+i) // (i+1) > r:
                r = (em+i) // (i+1)

        t = 0
        for i in range(n):
            if e[i] > r:
                t += e[i] - r

        rr.append('Case #{}: {} {}'.format(ti, r, t))

    return '\n'.join(rr)


print(main())
