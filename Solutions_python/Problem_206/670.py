#!/usr/bin/env python3

inf = float('inf')
read_ints = lambda : list(map(int, input().split()))

def solve(D, N, K, S):
    return min( [(S[i] * D) / (D-K[i]) for i in range(N)] )

if __name__ == '__main__':
    T = int(input())
    for t in range(1, T+1):
        D, N  = read_ints()
        X = [read_ints() for n in range(N)]
        K, S = zip(*X)
        print('Case #%d: %.6f' % (t, solve(D, N, K, S)))
