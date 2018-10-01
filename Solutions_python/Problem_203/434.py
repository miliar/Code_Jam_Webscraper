import numpy as np

t = int(raw_input())

for z in range(1,t+1):

    r,c = map(int, raw_input().split(' '))
    cake = []
    for i in range(r):
        cake.append(list(raw_input()))

    # print cake

    for i in range(r):
        for j in range(c):
            if(cake[i][j]!='?'):
                k = j-1
                while(cake[i][k]=='?' and k>=0):
                    cake[i][k]=cake[i][j]
                    k-=1

    # print cake

    for i in range(r):
        if(cake[i]==['?' for _ in range(c)]): continue
        if(cake[i][c-1]=='?'):
            k = c-1
            while(cake[i][k]=='?' and k>=0): k-=1
            p = cake[i][k]
            k+=1
            while(k<c and cake[i][k]=='?'):
                cake[i][k]=p 
                k+=1


    for i in range(r):
        for j in range(c):
            if(cake[i][j]=='?'):
                if(i>=1): cake[i][j] = cake[i-1][j]
                if(i==0): cake[i][j] = cake[i+1][j]

    cake = np.asarray(cake).T.tolist()
    
    # print cake

    for i in range(c):
        for j in range(r):
            if(cake[i][j]!='?'):
                k = j-1
                while(cake[i][k]=='?' and k>=0):
                    cake[i][k]=cake[i][j]
                    k-=1

    for i in range(c):
        if(cake[i]==['?' for _ in range(r)]): continue
        if(cake[i][r-1]=='?'):
            k = r-1
            while(cake[i][k]=='?' and k>=0): k-=1
            p = cake[i][k]
            k+=1
            while(k<r and cake[i][k]=='?'):
                cake[i][k]=p 
                k+=1



    cake = np.asarray(cake).T.tolist()

    print "Case #%d:" %(z)
    for i in range(r):
        print ''.join(cake[i])
