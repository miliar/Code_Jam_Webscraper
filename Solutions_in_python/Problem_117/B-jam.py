from string import *
T = input()
f = file('out.txt', 'w')
for Ti in range(1,T+1):
    inp = raw_input().strip().split()
    N = atoi(inp[0])
    M = atoi(inp[1])
    Ar=[[0]*M]*N
    Arout = [[0]*M]*N
    for i in range(N):
        Ar[i] = [int(j) for j in raw_input().strip().split()]
    #process
    for i in range(N):
        max = 0
        for j in range(M):
            if Ar[i][j] > max:
                max = Ar[i][j]
        Arout[i]=[max]*M
    #print Arout
    for j in range(M):
        max = 0
        for i in range(N):
            if Ar[i][j] > max:
                max = Ar[i][j]
        for i in range(N):
            if Arout[i][j]>max:
                Arout[i][j]=max
    #print Arout
    #judge
    out="YES"
    for i in range(N):
        for j in range(M):
            if Ar[i][j]!=Arout[i][j]:
                out="NO"
                break
    f.write("Case #"+str(Ti)+": "+out+"\n")
f.close()
