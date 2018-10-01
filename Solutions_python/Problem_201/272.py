def Stalls(N,K):
    if K==1:
        return (N/2,(N-1)/2)

    gen=len(bin(K))-3
    MX=N/2
    MN=(N-1)/2
    D=(MX,MN)
    if MX==MN:
        C=(2,0)
    else:
        C=(1,1)      
    
    for i in range(gen-1):
        mx1=MX/2
        mn1=(MX-1)/2
        mx2=MN/2
        mn2=(MN-1)/2
        c1,c2=0,0
        if mx1==mn1:
            c1=2*C[0]
            if mn1==mx2:
                c1+=C[1]
                if mx2==mn2:
                    c1+=C[1]
                else:
                    c2=C[1]
            else:
                c2=2*C[1]
        else:
            c1=C[0]
            c2=C[0]+2*C[1]
        C=(c1,c2)
        MX=mx1
        MN=mn2
    if K<2**gen+C[0]:
        sp=MX
    else:
        sp=MN
    print "sp ",sp    
    return (sp/2,(sp-1)/2)
    
out=open("out.txt","w")
with open("C-large.in") as file: #C-small-1-attempt0.in
    T=int(file.readline())
    for case in range(T):
        N,K=map(int,file.readline().rstrip().split())
        ans=Stalls(N,K)       
        #print ans
        #out.write(str(N)+"  "+str(K)+"\n")
        out.write("Case #"+str(case+1)+": "+str(ans[0])+" "+str(ans[1])+"\n")
out.close()