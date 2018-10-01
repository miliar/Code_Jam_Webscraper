#!/usr/bin/python3
__author__ = 'Tianren Liu'

import sys
import numpy as np

import scipy.optimize as op
import pulp
# op.linprog

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for t in range(1,T+1):
        N,M = map(int, sys.stdin.readline().split())
        table = np.full((N,N), ' ', dtype=str)
        xarray = np.zeros((N,N),  dtype=int)
        xset, yset = set(), set()
        darray = np.zeros((N,N), dtype=int)
        dset, idset = set(), set()

        upset = set() # updated points
        for _ in range(M):
            s,r,c = sys.stdin.readline().split()
            r,c = int(r)-1,int(c)-1
            table[r,c] = s
            if s == '+' or s == 'o':
                darray[r,c] = 1
                dset.add(r-c+N)
                idset.add(r+c)
            if s == 'x' or s == 'o':
                xarray[r,c] = 1
                xset.add(r)
                yset.add(c)

        for r,c in zip((i for i in range(N) if i not in xset), (i for i in range(N) if i not in yset)):
            xarray[r,c] = 1
            upset.add((r,c))

        freevar = [(r,c) for r in range(N) for c in range(N) if r-c+N not in dset and r+c not in idset]
        freevar.sort(key=lambda x:x[0]+x[1])
        while len(freevar) > 0:
            r,c = freevar[0] if sum(freevar[0]) < 2*N-2 - sum(freevar[-1]) else freevar[-1]
            darray[r,c] = 1
            dset.add(r-c+N)
            idset.add(r+c)
            upset.add((r,c))
            freevar = [(r,c) for r,c in freevar if r-c+N not in dset and r+c not in idset]

        # freevar = [(r,c) for r in range(N) for c in range(N) if r-c+N not in dset and r+c not in idset]
        # lpvar = {(r,c):pulp.LpVariable("v{}v{}".format(r,c),0,1) for r,c in freevar}
        # while len(freevar) > 0:
        #     ruleset = []
        #     d_rem, id_rem = [set() for _ in range(2*N)], [set() for _ in range(2*N)]
        #     for r,c in freevar:
        #         d_rem[r-c+N].add((r,c))
        #         id_rem[r+c].add((r,c))
        #
        #     progress = False
        #     for l in d_rem + id_rem:
        #         if len(l) = 0
        #         r,c = l
        #         darray[r,c] = 1
        #         dset.add(r-c+N)
        #         idset.add(r+c)
        #         upset.add((r,c))
        #         progress = True
        #         break
        #     if progress:
        #         freevar = [(r,c) for r,c in freevar if r-c+N not in dset and r+c not in idset]
        #         continue
        #     for rem, f in ((d_rem, lambda r,c:r+c), (id_rem, lambda r,c:r-c+N)):
        #         m = {}
        #         for l = d_rem:
        #             if len(l) == 2:
        #                 interval = min(l, key=f), max(l, key=f)
        #                 if interval in m:
        #                     pass
        #                 else:
        #                     m[interval] = (caty())
        #     # if (len(s_rem[0]) == 2):
        #     #     s_rem = [((min((r-c+N for r,c in s)), max((r-c+N for r,c in s))), s) for s in s_rem]
        #     #     s_rem.sort()
        #     #     progress = False
        #     #     for i in range(len(s_rem)-1):
        #     #         if s_rem[i][0] == s_rem[i+1][0]:
        #     #             progress = True
        #     #             r,c = min(s_rem,key=lambda v:v[0]-v[1])
        #     #             darray[r,c] = 1
        #     #             dset.add(r-c+N)
        #     #             idset.add(r+c)
        #     #             upset.add((r,c))
        #     #             break
        #     #     if progress:
        #     #         continue
        #
        #     for i in range(2*N):
        #         if len(d_rem[i]) > 0:
        #             ruleset.append([1 if r-c+N==i else 0 for r,c in freevar])
        #     for i in range(2*N):
        #         if len(id_rem[i]) > 0:
        #             ruleset.append([1 if r+c==i else 0 for r,c in freevar])
        #
        #     print(len(freevar))
        #     A = op.linprog(np.full(len(freevar), -1, dtype=float),
        #         A_ub=ruleset, b_ub=np.ones(len(ruleset)), bounds = [(0,1)]*len(freevar))
        #
        #     margin = .5/N
        #     for i in range(len(freevar)):
        #         if A.x[i] > margin:
        #             margin += 1-A.x[i]+.5
        #             r,c = freevar[i]
        #             darray[r,c] = 1
        #             dset.add(r-c+N)
        #             idset.add(r+c)
        #             upset.add((r,c))
        #
        #     freevar = [(r,c) for r,c in freevar if r-c+N not in dset and r+c not in idset]
        #     # break
        print("Case #{}: {} {}".format(t, darray.sum() + xarray.sum(), len(upset)))
        for r,c in upset:
            print("{} {} {}".format({0:'o', 1:'+', -1:'x'}[darray[r,c]-xarray[r,c]], r+1, c+1))
