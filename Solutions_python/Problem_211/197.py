def solve(n, k, u, p):
    # print n, k
    # print u
    p.sort()
    # print p
    if n == k:
        for i in range(n):
            # print i, u
            if i < n - 1 and u >= (i+1) * (p[i+1] - p[i]):
                u -= (p[i+1] - p[i]) * (i + 1)
            else:
                # print i, u
                v = u / (i + 1)
                totalp = min(p[i] + v, 1.0) ** (i+1)
                for j in range(i+1, n):
                    totalp *= p[j]
                return totalp
    return 0.0


def main():
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        n, k = [int(c) for c in raw_input().split(" ")]
        u = float(raw_input())
        p = [float(c) for c in raw_input().split(" ")]
        sol = solve(n, k, u, p)
        print "Case #{}: {:.6f}".format(i, sol)


if __name__ == "__main__":
    main()
