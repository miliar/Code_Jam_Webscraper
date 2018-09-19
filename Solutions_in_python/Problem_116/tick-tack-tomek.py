def check(A):
    flag=False
    for i in range(0,4): #columns
        var=A[0][i]
        if var=='.':
            flag=True
            continue
        elif var=='T':
            temp=A[1][i]
            for j in range(1,4):
                if temp=='.':
                    flag=True
                    break
                if A[j][i]=='.':
                    flag=True
                    break
                if A[j][i]!=temp: break
                if j==3:
                    print (temp, "won")
                    return
        else:
            for j in range(1,4):
                if A[j][i]=='T' and j!=3: continue
                if A[j][i]=='T' and j==3:
                    print (var, "won")
                    return
                if A[j][i]=='.':
                    flag=True
                    break
                if A[j][i]!=var: break
                if j==3:
                    print (var, "won")
                    return
    for i in range(0,4): #rows
        var=A[i][0]
        if var=='.':
            flag=True
            continue
        elif var=='T':
            temp=A[i][1]
            for j in range(1,4):
                if temp=='.':
                    flag=True
                    break
                if A[i][j]=='.':
                    flag=True
                    break
                if A[i][j]!=temp: break
                if j==3:
                    print (temp, "won")
                    return
        else:
            for j in range(1,4):
                if A[i][j]=='T' and j!=3: continue
                if A[i][j]=='T' and j==3:
                    print (var, "won")
                    return
                if A[i][j]=='.':
                    flag=True
                    break
                if A[i][j]!=var: break
                if j==3:
                    print (var, "won")
                    return
    #diagonals
    var=A[0][0]
    i=1
    if var=='.':
        flag=True
        i=4
    elif var=='T':
        var=A[1][1]
        i=2
    while i<4:
        if A[i][i]=='T' and i!=3: continue
        if A[i][i]=='T' and i==3:
            print (var, "won")
            return
        if var=='.':
            flag=True
            break
        if A[i][i]!=var: break
        if i==3:
            print(var, "won")
            return
        i+=1
    var=A[0][3]
    i=1
    if var=='.':
        flag=True
        i=4
    elif var=='T':
        var=A[1][2]
        i=2
    while i<4:
        if A[i][3-i]=='T' and i!=3: continue
        if A[i][3-i]=='T' and i==3:
            print (var, "won")
            return
        if var=='.':
            flag=True
            break
        if A[i][3-i]!=var: break
        if i==3:
            print(var, "won")
            return
        i+=1
    if flag:
        print ("Game has not completed")
    else:
        print ("Draw")
    return
        
    
f=open('input.in','r')        
A=[[],[],[],[]]
N=int(f.readline())
N=N*4+N
k=0
m=1
for i in range(0,N):
    stringer=f.readline()
    if len(stringer)>1:
        for j in range(0,4):
            A[k%4].append(stringer[j])
    else:
        print("Case #",m,":",sep='',end=' ')
        m+=1
        check(A)
        k-=1
        for j in range(0,4):
            A[j]=[]
    k+=1
    

f.close()


        
        
