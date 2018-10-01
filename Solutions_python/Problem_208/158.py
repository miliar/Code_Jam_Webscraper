def main():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        n, q = [int(s) for s in raw_input().split(" ")]
        es = [[int(s) for s in raw_input().split(" ")] for _ in range(n)]
        d = [[int(s) for s in raw_input().split(" ")] for _ in range(n)]
        uv = [[int(s) for s in raw_input().split(" ")] for _ in range(q)]

        print "Case #{}: {}".format(i, solve(n, q, es, d, uv))


def solve(n, q, es, d, uv):
    dd = [0]
    for i in range(1, n):
        dd.append(dd[i-1] + d[i-1][i])

    a = [0]
    for i in range(1, n):
        a.append(min(a[j] + (dd[i] - dd[j]) * 1. / es[j][1] for j in range(i) if es[j][0] >= dd[i] - dd[j]))

    return a[-1]


if __name__ == '__main__':
    main()
