fd=file('A-small.in')
T=int(fd.readline())
raw=map(lambda s: s.strip(),fd.readlines())
fd.close()
l1=[]
l2=[]
out=[]
for i in raw:
    if len(i)==1:
        l1+=[int(i) for i in i.split()]
    else:
        l2+=[int(i) for i in i.split()]
l2=[l2[i:i+4] for i in xrange(0,len(l2),4)]

def solution(case):
    counter=0
    res=[]
    for j in l2[((l1[0+2*i])+8*i)-1]:
        if j in l2[((l1[1+2*i])+4+8*i)-1]:
            counter+=1
            res+=[j]
    if counter==1:
        return "Case #%s: %s"%(i+1,res[0])
    elif counter>1:
        return "Case #%s: Bad magician!"%(i+1)
    else:
        return "Case #%s: Volunteer cheated!"%(i+1)

for i in xrange(T):
    out.append(solution(i))

fd=file('output.txt','w')
for s in out:
    fd.write(s+'\n')
fd.close()
