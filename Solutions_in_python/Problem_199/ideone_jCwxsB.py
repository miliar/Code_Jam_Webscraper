T = int(input())

for t in range(1, T+1):
    S, K = input().split()
    S = [c == '+' for c in S]
    K = int(K)

    flips = 0

    for i in range(len(S) - K + 1):
        c = S[i]
        #print(i, S)
        if not c:
            flips += 1
            for j in range(K):
                S[i+j] = not S[i+j]

    #print(S)

    if not all(S):
        flips = 'IMPOSSIBLE'

    print('Case #{}: {}'.format(t, flips))