#!/usr/bin/env python3

t = int(input())

for i in range(1, t+1):
    n = int(input())
    x = 1
    sub = 1
    while x <= n:
        a = (n//x)%10
        b = (n//(x*10))%10
        if a < b:
            n -= a*x + sub
            sub = n%(x*10) + 1
        else:
            sub += a*x
        x *= 10
    print('Case #{}: {}'.format(i, n))
