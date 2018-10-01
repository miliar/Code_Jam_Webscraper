file = open("B-small-attempt0.in")
l=[]
while 1:
    line=file.readline() 
    if not line:
        break
    l.append(line)
#l=['1','45 56 35']
#l=['5','3 4 2','4 5 2','7 8 5','45 56 35','103 143 88']
                
#print l
ptr=0
t=int(l[ptr])
ptr+=1
i=0
results=[]

while i<t:
    #print l
    nums=l[ptr]
    ptr+=1
    nL=nums.split()
    A=int(nL[0],10)
    B=int(nL[1],10)
    K=int(nL[2],10)
    count=0
    k=0
    while k<A:
        m=0
        while m<B:
            res=k&m
            #print str(k)+','+str(l)+','+str(res)
            if res<K:
                count+=1
            m+=1
        k+=1
    i+=1
    results.append("Case #"+str(i)+": "+str(count))

for e in results:
    print e
        
