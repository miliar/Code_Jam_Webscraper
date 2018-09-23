import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()


def main():
    t = I()
    r = []
    for ti in range(1,t+1):
        n,k = LI()
        a = [[n,1]]
        while a[0][1] < k:
            tn,tt = a[0]
            a = a[1:]
            tn -= 1
            t1 = tn//2
            t2 = tn - t1
            al = len(a)
            f = True
            for i in range(al):
                if a[i][0] == t1:
                    a[i][1] += tt
                    f = False
                    break
            if f:
                a.append([t1,tt])
            f = True
            for i in range(al):
                if a[i][0] == t2:
                    a[i][1] += tt
                    f = False
                    break
            if f:
                a.append([t2,tt])
            a = sorted(a, reverse=True)
            k -= tt

        tn = a[0][0] - 1
        tl = tn // 2
        tr = tn - tl

        r.append('Case #{}: {} {}'.format(ti,tr,tl))

    return '\n'.join(r)



print(main())
