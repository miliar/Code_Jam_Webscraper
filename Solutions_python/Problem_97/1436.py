fp=open('C-small-attempt0.in','r')
fw=open('C-small.out','w')
N=int(fp.readline())
for i in range(1,N+1):
    slist=fp.readline().split()
    a=int(slist[0])
    b=int(slist[1])
    ret=0
    lis=[]
    for q in range(a,b):
        if q>=10:
            for t in range(1,len(str(q))):
                ss=str(q)[t:len(str(q))]+str(q)[0:t]
                if int(ss) in range(a+1,b+1) and int(ss)>q:
                    ret+=1
                    if (ss+str(q)) not in lis:
                        lis.append(ss+str(q))
    fw.write("Case #"+str(i)+": "+str(len(lis)))
    fw.write('\n')
fw.close()
