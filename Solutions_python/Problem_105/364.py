T = int(raw_input())
for caseid in xrange(1,T+1):
    N = int(raw_input())
    A = [[0]*N for i in xrange(N)]
    for i in xrange(N):
        data = map(int,raw_input().split())
        for x in data[1:data[0]+1]:
            A[i][x-1]=1

    for k in xrange(N):
        for i in xrange(N):
            for j in xrange(N):
                A[i][j] += A[i][k]*A[k][j]

    res = "No"
    for row in A:
        for x in row:
            if x>1:
                res = "Yes"

    print "Case #%d: %s"%(caseid,res)
        
        
