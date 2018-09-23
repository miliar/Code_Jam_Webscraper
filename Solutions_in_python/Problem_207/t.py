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
        a = LI()
        n = a[0]
        a = a[1:]

        f = False
        if max(a) > n/2:
            f = True

        for i in range(6):
            if a[i] > n - (a[i-2] + a[(i-3)] + a[i-4]):
                f = True

        if f:
            rr.append('Case #{}: IMPOSSIBLE'.format(ti))
            continue

        r = []
        for iii in range(6):
            if a[iii] < 1:
                continue
            t = a[:]
            r = [iii]
            a[iii] -= 1
            for ii in range(n-1):
                mj = -1
                mm = 0
                for i in range(6):
                    if a[i] < 1 or mm >= a[i] + a[i-1] + a[(i+1)%6]:
                        continue
                    if r[-1] != (i-1)%6 and r[-1] != (i+1)%6 and r[-1] != i:
                        mm = a[i] + a[i-1] + a[(i+1)%6]
                        mj = i

                if mj < 0:
                    r = []
                    break

                a[mj] -= 1
                r.append(mj)

            if abs(r[0] - r[-1]) < 2:
                r = []

            if r:
                break

        if not r:
            rr.append('Case #{}: IMPOSSIBLE'.format(ti))
            continue

        rr.append('Case #{}: {}'.format(ti, ''.join(map(lambda x: ra[x], r))))

    return '\n'.join(rr)

print(main())
