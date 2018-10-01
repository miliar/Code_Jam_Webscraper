from __future__ import division
import fileinput
from operator import itemgetter
import math

pi = math.pi

def max_height(L, i, h, n, K):
    if n == K:
        raise RuntimeError("Problem.")

    if i == len(L) - 1:
        # Last item.
        if n < K - 1:
            return 0 # Cannot take enough items.
        else:
            return L[i][1]

    take = max_height(L, i + 1, h + L[i][1], n + 1, K)
    not_take = max_height(L, i + 1, h, n + 1, K)


def main():
    fin = fileinput.input()
    T = int(next(fin))  # number of test cases
    for case in range(1, T + 1):
        N, K = map(int, next(fin).split(' '))
        L = [[0, 0, 0] for i in range(N)]
        for i in range(N):
            L[i][0], L[i][1] = map(int, next(fin).split(' '))
            L[i][2] = 2 * L[i][0] * L[i][1] * pi

        # if case == 69:
        #     print N, K, L

        L = sorted(L, key=itemgetter(0))
        T = [[0 for i in range(N)] for k in range(K)]
        T[0][0] = L[0][2]
        for i in range(1, N):
            T[0][i] = max(L[i][2], T[0][i - 1])
        for k in range(1, K):
            for i in range(k, N):
                T[k][i] = max(L[i][2] + T[k - 1][i - 1], T[k][i - 1])

        m = 0.
        for i in range(N):
            temp = L[i][2] + pi * L[i][0] * L[i][0]
            if K == 1 or i == 0:
                m = max(m, temp)
            else:
                m = max(m, temp + T[k - 1][i - 1])
        print("Case #{0}: {1:.9f}".format(case, m))

if __name__ == "__main__":
    main()