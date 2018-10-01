T = int(raw_input())
for t in xrange(T):
    print "Case #"+str(t+1)+":",
    n,m = map(int,raw_input().split())
    grass = []
    for i in xrange(n):
        grass.append(map(int,raw_input().split()))
    zgrass = [[grass[i][j] for i in xrange(n)] for j in xrange(m)]
    cols = map(max,zgrass)
    rows = map(max,grass)
    good = True
    for i in xrange(n):
        for j in xrange(m):
            if grass[i][j] != rows[i] and grass[i][j]!=cols[j]:
                good = False
                print "NO"
                break
        if (not good):
            break
    if good:
        print "YES"
        

