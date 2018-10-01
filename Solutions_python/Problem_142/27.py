fin=open("A-large.in","r")
fout=open("Output.out","w")
T=int(fin.readline())
Ans=""
for t in range(T):
    Ans+="Case #"+str(t+1)+": "
    N=int(fin.readline())
    S=[]
    for i in range(N):
        S.append(fin.readline().split()[0])
    F=[]
    for j in range(N):
        p=S[j][0]
        cnt=1
        F.append([])
        for i in range(1,len(S[j])):
            if(S[j][i]==p):
                cnt+=1
            else:
                F[-1].append((p,cnt))
                p=S[j][i]
                cnt=1
        F[-1].append((p,cnt))
    x=len(F[0])
    valid=True
    for i in range(N):
        if(len(F[i])!=x):
            Ans+="Fegla won\n"
            valid=False
            break
    if(not valid):
        continue
    E=[]
    for i in range(len(F[0])):
        X=[]
        p=F[0][i][0]
        for j in range(N):
            if(F[j][i][0]!=p):
                Ans+="Fegla Won\n"
                valid=False
                break
            X.append(F[j][i][1])
        if(not valid):
            break
        E.append(X)
    if(not valid):
        continue
    ans=0
    for item in E:
        e=max(item)
        ee=min(item)
        b=0
        for q in range(ee,e+1):
            temp=0
            for z in item:
                temp+=abs(q-z)
            if(q==ee):
                b=temp
            else:
                b=min(temp,b)
        ans+=b
    Ans+=str(ans)+"\n"
fout.write(Ans)
fout.close()
