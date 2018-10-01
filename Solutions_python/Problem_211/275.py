from __future__ import division
import fileinput
from operator import itemgetter
import math

pi = math.pi


def main():
    fin = fileinput.input()
    T = int(next(fin))  # number of test cases
    for case in range(1, T + 1):
        N, K = map(int, next(fin).split(' '))
        U = float(next(fin))
        L = map(float, next(fin).split(' '))
        L = sorted(L, reverse=True)

        suma = sum(L)
        for i in range(N):
            sl = L[i:]
            mn = (sum(sl) + U ) / len(sl)
            if mn >= sl[0]:
                for k in range(i, N):
                    L[k] = mn
                break
        prod = 1.0
        for i in range(N):
            prod *= L[i]

        print("Case #{0}: {1:.9f}".format(case, prod))

if __name__ == "__main__":
    main()
