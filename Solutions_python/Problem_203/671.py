#!/bin/python
import itertools

def solve(S, K, count):
    if len(S) == 0: return str(count)
    if len(S) < K: return 'IMPOSSIBLE'
    # print S, K, count

    left = 0
    right = len(S) - 1
    if not S[left]:
        for i in range(left, left + K):
            S[i] = not S[i]
        count += 1

    if not S[right]:
        for i in range(right - K + 1, right + 1):
            S[i] = not S[i]
        count += 1

    # print S, K, count
    while left < len(S) and S[left]: left += 1
    while right >= 0 and S[right]: right -= 1
    # print left, right
    return solve(S[left:right + 1], K, count)



T = int(raw_input().strip())

for c in range(1, T + 1):
    R, C = map(int, raw_input().split())
    cake = [list(raw_input()) for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if cake[i][j] != '?':
                initial = cake[i][j]
                k=j+1
                while k < C and cake[i][k] == '?':
                    cake[i][k] = initial
                    k += 1

    for i in range(R):
        for j in range(C):
            if cake[i][j] != '?':
                initial = cake[i][j]
                k = j-1
                while k>=0 and cake[i][k] == '?':
                    cake[i][k] = initial
                    k -= 1

    for i in range(R):
        for j in range(C):
            if cake[i][j] != '?':
                initial = cake[i][j]
                k = i + 1
                while k < R and cake[k][j] == '?':
                    cake[k][j] = initial
                    k += 1

    for i in range(R):
        for j in range(C):
            if cake[i][j] != '?':
                initial = cake[i][j]
                k = i - 1
                while k >=0 and cake[k][j] == '?':
                    cake[k][j] = initial
                    k -= 1

    ans = '\n'.join([''.join(a) for a in cake])

    # S, K = raw_input().split()
    # S = map(lambda x: False if x == '-' else True, S)
    # K = int(K)
    # ans = solve(S, K, 0)
    print 'Case #' + str(c) + ':\n' + ans
