finame='C-small-attempt0.in'
foname='C-small-attempt0.out'
fi=open(finame,'r')
fo=open(foname,'w')

t=int(fi.readline())
for count in range(t):
    line=fi.readline()
    line=line.strip()
    line=line.split()
    r=int(line[0])
    k=int(line[1])
    n=int(line[2])
    line=fi.readline()
    line=line.strip()
    group=line.split()
    for i in range (n):
        group[i]=int(group[i])
        
    money=0
    for i in range (r):
        remain=k
        j=0
        while j<len(group) and (remain-group[j]>=0):
            remain-=group[j]
            money+=group[j]
            j+=1
   
        for a in range(j):
            group.append(group.pop(0))
 
    fo.write('Case #%d: %d\n'%(count+1,money))
fi.close()
fo.close()