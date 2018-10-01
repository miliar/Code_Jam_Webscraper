import math


def main():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        n, k = [int(s) for s in raw_input().split(" ")]
        cakes = [[int(s) for s in raw_input().split(" ")] for _ in range(n)]

        print "Case #{}: {}".format(i, solve(cakes, n, k))


def solve(cakes, n, k):
    cakes.sort(reverse=True)

    m = s = 0
    for i in range(n - k + 1):
        arr = [cakes[j][0]*cakes[j][1] for j in range(i + 1, n)]
        arr.sort(reverse=True)
        s = 2 * math.pi * (cakes[i][0] * cakes[i][1] + sum(arr[:k-1])) + math.pi * cakes[i][0] * cakes[i][0]
        m = max(m, s)

    return m


if __name__ == '__main__':
    main()
