d = {}


def solve_recursion(n, k):
    if k == n:
        return 0, 0
    elif k == 1:
        if n % 2 == 1:
            return n / 2, n / 2
        else:
            return n / 2, n / 2 - 1

    if (n, k) in d:
        return d[(n, k)]

    if n % 2 == 1:
        d[(n, k)] = solve_recursion(n / 2, k / 2)
    else:
        # n % 2 == 0
        if k % 2 == 1:
            d[(n, k)] = solve_recursion(n / 2 - 1, k / 2)
        else:
            d[(n, k)] = solve_recursion(n / 2, k / 2)
    return d[(n, k)]


def solve(n, k):
    return solve_recursion(n, k)


assert solve(3, 2) == (0, 0)
assert solve(4, 2) == (1, 0)
assert solve(5, 2) == (1, 0)
assert solve(6, 2) == (1, 1)
assert solve(1000, 1000) == (0, 0)
assert solve(1000, 1) == (500, 499)
assert solve(1000000, 1000000) == (0, 0)
assert solve(1000000000000000000, 1000000000000000000) == (0, 0)
for t in range(1, int(raw_input()) + 1):
    n, k = map(int, raw_input().strip().split())
    sol = solve(n, k)
    print 'Case #%d: %d %d' % (t, sol[0], sol[1])
