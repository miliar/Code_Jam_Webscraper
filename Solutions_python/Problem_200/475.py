from __future__ import print_function, unicode_literals


def solve(n):
    if n < 10:
        return n

    last = n % 10

    m = n / 10
    while m > 0:
        if m % 10 > last:
            last = 9
            n -= 10
            break
        m /= 10

    s = solve(n / 10) * 10
    if s % 100 == 90:
        last = 9
    return s + last


if __name__ == '__main__':
    T = int(raw_input())
    for Ti in range(T):
        n = int(raw_input())
        ans = solve(n)
        print("Case #{}: {}".format(Ti + 1, ans))
