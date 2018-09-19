T=int(raw_input())

for t in range(1,T+1):
    A=[]
    N,M=[int(x) for x in raw_input().split()]
    for n in range(N):
       A.append([int(x) for x in raw_input().split()])
    
    B=[list(i) for i in zip(*A)]
    maxA=[max(x) for x in A ]
    maxB=[max(x) for x in B ]
    flag=0
    for i in range(N):
        for j in range(M):
            if A[i][j] == min(maxA[i],maxB[j]):
                continue
            else:
                print "Case #"+str(t)+": "+"NO"
                flag=1
                break
        if flag==1:
            break
    
    if i==N-1 and j==M-1 and flag==0:
        print "Case #"+str(t)+": "+"YES"
