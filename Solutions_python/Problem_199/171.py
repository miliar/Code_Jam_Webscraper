T = int(input())
for tid in range(T):
    C, K = input().split(' ')
    K = int(K)
    result = 0
    S = []
    for a in C:
        S.append(a)
    for i in range(len(S) - K + 1):
        if S[i] == '-':
            result += 1
            for j in range(K):
                if S[i + j] == '-':
                    S[i + j] = '+'
                else:
                    S[i + j] = '-'
    for i in range(len(S) - K + 1, len(S)):
        if S[i] == '-':
            result = 'IMPOSSIBLE'
    print('Case #{}: {}'.format(tid + 1, str(result)))
