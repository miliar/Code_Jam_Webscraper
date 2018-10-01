for i in xrange(1, input()+1):
    R, C = [int(x) for x in raw_input().split()]
    G = [None]*R
    for j in xrange(R):
        G[j] = list(raw_input())
    
    for j in xrange(R):
        for k in xrange(C):
            if G[j][k] == '?':
                continue
            if (j>0 and G[j][k] == G[j-1][k]) or (k>0 and G[j][k] == G[j][k-1]):
                continue
            ik, fk = k, k+1
            for dk in xrange(k-1, -1, -1):
                if G[j][dk] == '?':
                    G[j][dk] = G[j][k]
                    ik-=1
                else:
                    break    
            for dk in xrange(k+1, C):
                if G[j][dk] == '?':
                    G[j][dk] = G[j][k]
                    fk+=1
                else:
                    break
            for dj in xrange(j-1, -1, -1):
                onlyQ = True
                for l in G[dj][ik:fk]:
                    if l != '?':
                        onlyQ = False
                        break
                if onlyQ:
                    for dk in xrange(ik, fk):
                        G[dj][dk] = G[j][k]
                else:
                    break
            for dj in xrange(j+1, R):
                onlyQ = True
                for l in G[dj][ik:fk]:
                    if l != '?':
                        onlyQ = False
                        break
                if onlyQ:
                    for dk in xrange(ik, fk):
                        G[dj][dk] = G[j][k]
                else:
                    break
    
    for j in xrange(R):
        G[j] = ''.join(G[j])
    G = '\n'.join(G)
    print "Case #%d:"%i
    print G