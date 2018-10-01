#! /usr/bin/python3

T = int(input())

for case_id in range(1, T + 1):
    N, S = input().split()
    N = int(N)
    S = [int(s) for s in S]

    standing = 0
    needed = 0
    for idx, s in enumerate(S):
        if not s:
            continue
        elif standing >= idx:
            standing += s
        else:
            extra = idx - standing
            needed += extra
            standing += s + extra
    print("Case #{0}: {1}".format(case_id, needed))
