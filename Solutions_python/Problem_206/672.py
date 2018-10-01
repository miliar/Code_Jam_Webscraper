rnd="p17R1B"
pb="A"
size="large(1)"
fin=open("C:\F\workspace\Euler\EulerProject\GCJam\%s\%s-%s.in"%(rnd,pb,size),'r')
fout=open("C:\F\workspace\Euler\EulerProject\GCJam\%s\%s-%s.out"%(rnd,pb,size),'w')

T=int(fin.readline())
print T
for i in range(1,T+1):
    sD,sN=fin.readline().strip().split()
    D,N=float(sD),int(sN)
    Hs=[]
    for j in range(N):
        sK,sS=fin.readline().strip().split()
        K,S=float(sK),float(sS)
        Hs.append((K,S))
    res=D/(max([((D-k)/s) for (k,s) in Hs]))
    
        
        

            
    line="Case #%d: %.6f" % (i, res)
    print line
    fout.write(line+"\n")
fout.close()