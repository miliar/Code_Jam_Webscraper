def solve():
    f = open('A-large.in')
    g = open('A.out','w')
    N = int(f.readline())
    for i in range(N):
        S = int(f.readline())
        se = []
        for j in range(S): se += [f.readline()]
        Q = int(f.readline())
        qs = []
        for j in range(Q): qs += [f.readline()]
        m = [[0]*S]*(Q+1)
        for k in range(Q):
            for j in range(S):
                if se[j]!=qs[k] : m[k+1][j] = m[k][j]
                else : m[k+1][j] = min(m[k][0:j] + m[k][j+1:]) + 1
        g.write('Case #'+str(i+1)+': '+str(min(m[Q]))+'\n')
    f.close()
    g.close()
solve()