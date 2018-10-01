import sys

def test(N, K):
    if K == N:
        return 0, 0

    n = N - 1

    l = n / 2
    r = n - l

    k = K - 1

    k_l = k / 2
    k_r = k - k_l

    if K == 1:
        return r, l

    if K == 2:
        return test(r, 1)

    if n % 2 == 0:
        return test(r, k_r)
    else:
        if k % 2 == 0:
            return test(l, k_l)
        else:
            return test(r, k_r)

total = None
cases = 0

for line in sys.stdin:
    if total:
        cases = cases+1
        args = line.split()
        right, left =  test( int(args[0]), int(args[1]) )

        sys.stdout.write('Case #' + str(cases) + ': ' + str(right) + ' ' + str(left) + '\n')
    else:
        total = line
