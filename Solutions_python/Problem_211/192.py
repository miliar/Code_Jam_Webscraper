import sys
from decimal import Decimal

T = int(sys.stdin.readline().strip())

for t in range(T):
    N, K = [int(i) for i in sys.stdin.readline().split()]
    U = Decimal(sys.stdin.readline().strip())

    P = [Decimal(i) for i in sys.stdin.readline().split()]

    # assuming K = N

    P.sort()

    for p in range(len(P)-1):
        core = P[p]
        core_above = P[p+1]

        shares = p+1
        distance = core_above-core
        total = min(distance*shares, U)

        share_size = total / Decimal(shares)

        for p2 in range(p+1):
            P[p2] += share_size
            U -= share_size

    if U > Decimal(0.0):
        shares = N
        share_size = U / Decimal(shares)

        for p in range(len(P)):
            P[p] += share_size
            U -= share_size

    answer = Decimal(1.0)
    for p in P:
        answer *= p
    print("Case #{0}: {1:f}".format(t+1, float(answer)))

