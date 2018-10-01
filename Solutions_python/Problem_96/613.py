import collections

inf = open("B-large.in")
outf = open("B-large.out", "w")

def nmax(a, b, add):
    if b == -1:
        return a
    return max(a, b + add)

def maxGooglers(N, S, p, sums):
    am = [[None] * (S + 1) for _ in range(N + 1)]
    def doMagic(googler, surp):
        if googler == N:
            return 0 if surp == S else -1
        if am[googler][surp] is not None:
            return am[googler][surp]
        res = -1
        for first in range(0, 11):
            for second in range(first, 1 + min(10, first + 2)):
                third = sums[googler] - first - second
                if not (0 <= third <= 10):
                    continue
                delta = max(abs(first - third), abs(first - second), abs(second - third))
                scored = 1 if max(first, second, third) >= p else 0
                if delta <= 1:
                    res = nmax(res, doMagic(googler + 1, surp), scored)
                elif delta == 2 and surp < S:
                    res = nmax(res, doMagic(googler + 1, surp + 1), scored)

        am[googler][surp] = res
        return res
    return doMagic(0, 0)


numTests = int(inf.readline().rstrip())

for test in range(numTests):
    args = list(map(int, inf.readline().split()))
    N, S, p = args[:3]
    sums = args[3:]
    print("Case #%d: %d" % (test + 1, maxGooglers(N, S, p, sums)), file=outf)

