import math
fin=open("stall.in","r")
fout=open("stall.out","w")
T=int(fin.readline())
for dummy in range(T):
    fout.write("Case #"+str(dummy+1)+": ")
    [N,K]=[int(x) for x in fin.readline().split()]
    D={N:1}
    m=(N-1)/2
    M=m+(N-1)%2
    while K>0:
        if 0 in D:
            del D[0]
        A=list(D)
        A.sort(key=lambda x:(-1)*x)#A is from largest to smallest
        B=[A[0]]
        for t in B:
            m=(t-1)/2
            M=m+(t-1)%2
            if m in D:
                D[m]+=D[t]
            else:
                D[m]=D[t]
            if M in D:
                D[M]+=D[t]
            else:
                D[M]=D[t]
            K=K-D[t]
            del D[t]
            if K<=0:
                break
    fout.write(str(M)+' '+str(m)+'\n')

        
    
    
