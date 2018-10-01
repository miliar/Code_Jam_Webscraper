f=open('B-small-attempt0.in')
g=open('result.in','w')
T=int(f.readline())
for case in range(1,T+1):
    A,B,K=map(int,f.readline().split())
    s=0
    for a in range(A):
        for b in range(B):
            if a&b<K:
                s+=1
    g.write('Case #'+str(case)+': '+str(s)+'\n')
g.close()
f.close()
                
