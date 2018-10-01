#!/usr/bin/python3
t = int(input())

for it in range(1, t+1) :
    n = int(input())
    a = 1
    while a * 10 + 1 <= n:
        a = a * 10 + 1
    k = min(n // a, 9)
    ans = a * k
    while k < 9:
        while ans + a > n:
            a = a // 10
        ans += a
        k += 1
    print("Case #%d:"%it, ans)
