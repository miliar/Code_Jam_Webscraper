import sys
T = int(sys.stdin.readline().strip())

for t in range(1, T+1):
    S, K = sys.stdin.readline().strip().split()
    S = list(S)
    K = int(K)
    count = 0
    for i in range(len(S)-K+1):
        if S[i] == '-':
            for j in range(i, i+K):
                S[j] = '+' if S[j] == '-' else '-'
            count += 1
    if '-' in S:
        print('Case #{}: {}'.format( t, 'IMPOSSIBLE'))
    else:
        print('Case #{}: {}'.format( t, count))
        
