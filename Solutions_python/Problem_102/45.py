def passes(N, s, i, p, J):
    missing = 0
    lonely = True
    score = s[i] + (p * J)
    for j in range(N):
        if j != i:
            if s[j] <= score:
                lonely = False
                missing += score - s[j]
    return missing + p * J >= J and not lonely

def solve(N, s):
    J = sum(s)
    m = [0 for i in range(N)]
    for i in range(N):
        mini, maxi = 0, 1
        while maxi - mini > 10 ** - 9:
            mid = (mini + maxi) / 2
#            print(mid)
            if passes(N, s, i, mid, J):
                mini, maxi = mini, mid
            else:
                mini, maxi = mid, maxi
        m[i] = mid
    return m

T = int(input ())
for i in range(1, T + 1):
    N, *s = map(int, input().split())
    print("Case #%d:" % i, end="")
    for mi in solve(N, s):
        print(" %3.6f" % (mi * 100), end="")
    print()

#print(passes(2, [20, 10], 0, 0, 30))
