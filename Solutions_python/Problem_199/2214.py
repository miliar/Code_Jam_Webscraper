T = int(input())
with open('A.out', 'w+') as fout:
    for t in range(T):
        S, K = input().split()
        K = int(K)
        print('case %d: S = %s'%(t+1,S))
        i = 0
        while not all([s=='+' for s in S]):
            p = S.find('-')
            if p > len(S)-K:
                break
            S = S[:p] + ''.join(['-' if c == '+' else '+' for c in S[p:p+K]]) + S[p+K:]
            i += 1
        if not all([s=='+' for s in S]): fout.write('Case #%d: IMPOSSIBLE\n'%(t+1))
        else: fout.write('Case #%d: %d\n'%(t+1,i))
