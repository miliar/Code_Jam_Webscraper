fin=open("B-large.in","r")
fout=open("B-large.out","w")
ca=int(fin.readline())
for cas in xrange(1,ca+1):
    fout.write("Case #"+str(cas)+": ")
    arg=map(int,fin.readline().split())
    n=arg[0]
    k=arg[1]
    b=arg[2]
    t=arg[3]
    c=map(int,fin.readline().split())
    m=map(int,fin.readline().split())
    can=[]
    num=0
    
    for i in xrange(n):
        if(m[i]*t+c[i]>=b):
            can.append(True)
            num+=1
        else:
            can.append(False)

    index=n
    done=0
    ans=0
    boom=0
    
    while(done<k and index>0):
        
        index-=1
        if(can[index]):
            ans+=boom
            done+=1
        else:
            boom+=1
    if(done<k):
        fout.write("IMPOSSIBLE\n")
    else:
        fout.write(str(ans)+"\n")
fin.close()
fout.close()
                
        
