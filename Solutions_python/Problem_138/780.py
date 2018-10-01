fl=open('D-large.in','r+')
t=int(fl.readline())
def calculate1(a,b):
    a.sort(reverse=True)
    b.sort()
    count=0
    for i in a:
        val=-1
        for j in b:
            if j > i:
                val=j
                break
        if val==-1:
            b.remove(b[0])
            count+=1
        else:
            b.remove(val)
    return count

def calculate2(a,b):
    a.sort()
    b.sort()
    count=0
    for i in b:
        val=-1
        for j in a:
            if j>i:
                val=j
                break
        if val==-1:
            break
        else:
            a.remove(val)
            count+=1
    b=b[len(b)-len(a):]
    return count+calculate1(a,b)
            
                
        
for case in xrange(t):
    n=int(fl.readline())
    nm=[float(e) for e in fl.readline().split()]

    kn=[float(e) for e in fl.readline().split()]

    n1=calculate2(nm+[],kn+[])
    n2=calculate1(nm,kn)
    print 'Case #%d: %d %d'%(case+1,n1,n2)
