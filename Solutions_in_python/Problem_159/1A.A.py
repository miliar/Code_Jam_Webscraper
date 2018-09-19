# Python 3
import scipy as sc

if __name__ == '__main__':
    T = int(input())

    for i in range(T):
        N = int(input())
        M = sc.array(list(map(int, input().split())))
        diffs = sc.array(list(M[x-1] - M[x] for x in range(1, M.size)))
        # using first method
        a1 = sum(x for x in diffs if x > 0)
        # using second method
        rate = diffs.max()
        a2 = 0
        for x in M[:-1]:
            a2 += min(rate, x)

        print("Case #" + str(i+1) + ": " + str(a1) + " " + str(a2))

