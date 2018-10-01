# This code was interpreted using CPython 3.3.4
# python3 Main.py < data.in > data.out

import decimal

T = int(input())
for T_ in range(1, T+1):
    S = decimal.Decimal(2)
    C, F, X = [decimal.Decimal(x) for x in input().split(' ')]

    best_time = X/S
    last_time = decimal.Decimal(0)
    while True:
        last_time += C/S
        S += F

        if last_time + X/S < best_time:
            best_time = last_time + X/S
        else:
            break

    print("Case #{0}: {1:.7f}".format(T_, best_time))