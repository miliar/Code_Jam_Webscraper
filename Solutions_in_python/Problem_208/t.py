import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy

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
    rr = []
    tt = I()
    ra = "ROYGBV"
    for ti in range(1,tt+1):
        n,q = LI()
        e = []
        s = []
        r = []
        for _ in range(n):
            et, st = LI()
            e.append(et)
            s.append(st)
        d = [LI() for _ in range(n)]
        for _ in range(q):
            u,v = LI_()
            if _ > 1:
                break
            a = [inf] * n
            a[u] = 0
            for i in range(n-1):
                t = a[i]
                k = e[i]
                for j in range(i+1,n):
                    k -= d[j-1][j]
                    if k < 0:
                        break
                    t += d[j-1][j] / s[i]
                    if a[j] > t:
                        a[j] = t
            r.append(a[v])

        rr.append('Case #{}: {}'.format(ti, ' '.join(map(lambda x: str(x), r))))

    return '\n'.join(rr)

print(main())
