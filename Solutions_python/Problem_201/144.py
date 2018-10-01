s = {}
def solve(n, k):

    if k == 0:
        return (n, n)

    if k == 1:
        return (n / 2, (n - 1) / 2)

    if (n, k) in s:
        return s[(n, k)]

    max1, min1 = solve((n - 1) / 2, (k - 1) / 2)
    max2, min2 = solve(n / 2, k / 2)

    ret = (min(max1, max2), min(min1, min2))
    s[(n, k)] = ret
    return ret

t = int(input())
for case in range(1, t + 1):

    n, k = [int(x) for x in raw_input().split(" ")]

    maxL, minL = solve(n, k)

    print("Case #{}: {} {}".format(case, maxL, minL))
