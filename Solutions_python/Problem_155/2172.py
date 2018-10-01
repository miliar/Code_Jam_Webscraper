dead=open("A-large.in")
n=dead.readline()
n.replace('\n','')
n=int(n)
res=[]
def toed(c, a, p):
    f=0
    s=int(p[0])
    for i in range(1,a+1):
        if s>=i:
            s+=int(p[i])
        else:
            f+=i-s
            s+=int(p[i])+i-s
    return "Case #"+str(c)+": "+str(f)
for i in range(n):
    x=(dead.readline())
    x.replace('\n','')
    x=x.split(' ')
    res.append(toed(i+1,int(x[0]),x[1]))
dead.close()
alive=open("A-large.out",mode='w')
for el in res:
    alive.write(el+'\n')
alive.close()
