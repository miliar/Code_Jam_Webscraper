import sys

fin = sys.stdin
T = int(fin.readline())

for t in xrange(1, T + 1):
    N, M = map(int, fin.readline().split())
    root = {}
    ans = 0
    for i in xrange(N):
        direc = fin.readline().strip().split('/')
        parent = root
        for d in direc[1:]:
            if parent.has_key(d):
                parent = parent[d]
            else:
                parent[d] = {}
                parent = parent[d]

    for j in xrange(M):
        make = fin.readline().strip().split('/')
        parent = root
        for d in make[1:]:
            if parent.has_key(d):
                parent = parent[d]
            else:
                parent[d] = {}
                parent = parent[d]
                ans += 1
                #print 'making', d

    print 'Case #' + str(t) + ':', ans
