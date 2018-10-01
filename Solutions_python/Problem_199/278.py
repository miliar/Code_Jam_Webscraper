def solve(S, K):
    if K > len(S):
        return 'IMPOSSIBLE'

    step = 0

    for i in xrange(len(S) - K + 1):
        if S[i] == '+':
            continue

        step += 1
        for j in xrange(K):
            k = i + j
            if S[k] == '+':
                S[k] = '-'
            else:
                S[k] = '+'

    for i in xrange(K):
        if S[-i] == '-':
            return 'IMPOSSIBLE'
    
    return step



T = int(raw_input())

for i in xrange(T):
    S, K = raw_input().split()
    K = int(K)
    S = [x for x in S]

    print 'Case #%d: %s' % (i + 1, solve(S, K))

    
