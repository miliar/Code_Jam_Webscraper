for Pr in xrange(1, input()+1):
    N, K = [int(x) for x in raw_input().split()]
    U = float(raw_input())
    P = [float(x) for x in raw_input().split()]
    P.sort()
    P.reverse()
    S = sum(P)
    S += U
    t = K
    for i in xrange(K):
        A = S/(K-i)
        if A<P[i]:
            S -= P[i]
        else:
            t=i
            break
    if t<K:
        A = S/(K-t)
        for i in xrange(t, K):
            P[i] = A
    prod = 1
    for p in P:
        prod *= p
    print 'Case #%d: %f'%(Pr, prod)