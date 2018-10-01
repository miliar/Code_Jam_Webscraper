from os import*

f=file('A-large.in','r+')
o=file('sout','w')
l=f.readlines()
case_count=int(l[0])
l=l[1:]
    
def foo(l):
    scount=0
    egs=l[1:int(l[0])+1]
    qs=l[int(l[0])+2:int(l[0])+2+int(l[int(l[0])+1])]
    while(True):
        maxv=0
        for eg in egs:
            try:
                v=qs.index(eg)
            except:
                return scount
            if v>maxv:
                maxv=v
        scount+=1
        qs=qs[maxv:]

for i in range(1,case_count+1):
    o.write('Case #'+str(i)+': '+str(foo(list(l)))+'\n')
    l=l[int(l[0])+2+int(l[int(l[0])+1]):]
f.close()
o.close()