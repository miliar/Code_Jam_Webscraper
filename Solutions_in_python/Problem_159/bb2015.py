T=int(input())
for t in range(0,T):
    N=int(input())
    m2=0
    t1=0
    M = [int(x) for x in input().split(" ")]
    for i in range(1,len(M)):
        if M[i] < M[i-1]:
            m1=M[i-1]-M[i]
            if m1>m2:
                m2=m1
            t1+=m1
    t2=0
    for i in range(0,len(M)-1):
        m1=M[i-1]-M[i]
        if m2>M[i]:
            t2+=M[i]
        else:
            t2+=m2
    print('Case #%d: %d %d'%(t+1,t1,t2))
