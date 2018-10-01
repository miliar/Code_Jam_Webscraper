def dfs(mat,mark,p,ind):
    if(ind == p):
        return 0
    else:
        ans = dfs(mat,mark,p,ind+1)
        for i in mat[ind]:
            if(mark[i]==0):
                mark[i]=1
                ans = max(ans,1+dfs(mat,mark,p,ind+1))
                mark[i]=0
        return ans
def prog():
    n,p = map(int,raw_input().split())
    if(n==1):
        x = input()
        mx,Mx = x*0.9,x*1.1
        gx = [float(x) for x in raw_input().split()]
        cnt = 0
        for i in gx:
            z = int(i/mx)
            Z = int(i/Mx)
            nn = 0
            for k in xrange(Z,z+5):
                ok = False
                if(i>=k*mx and i<=k*Mx):
                    ok = True
                if(ok==True):
                    nn = max(nn,k)
            if(nn!=0):
                cnt+=1
        print cnt
    elif(n==2): 
        x,y = map(int,raw_input().split())
        mx,Mx = x*0.9,x*1.1
        my,My = y*0.9,y*1.1
        gx = [float(x) for x in raw_input().split()]
        gy = [float(x) for x in raw_input().split()]
        mat = []
        for i in xrange(p):
            mat += [[]]
        for i in xrange(p):
            for j in xrange(p):
                z = int(gx[i]/mx)
                Z = int(gx[i]/Mx)
                nn = 0
                for k in xrange(Z,z+5):
                    ok = False
                    if(gx[i]>=k*mx and gx[i]<=k*Mx):
                        if(gy[j]>=k*my and gy[j]<=k*My):
                            ok = True
                    if(ok==True):
                        nn = max(nn,k)
                if(nn!=0):
                    mat[i]+=[j]
        mark=[0]*p
        print dfs(mat,mark,p,0)               
    else:
        print 0                   
t = input()
for T in xrange(1,t+1):
    print "Case #"+str(T)+":",
    prog()
