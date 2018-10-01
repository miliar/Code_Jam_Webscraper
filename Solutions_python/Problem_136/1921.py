__author__ = 'majid'
def func(c,f,x,n):
    s=0
    for i in range(n+1):
        s=s+c/(2+i*f)
    s=s+x/(2+(n+1)*f)
    return s;
def g(c,f,x):
    l=[x/2]
    l.append(func(c,f,x,0))
    i=1
    while l[-2]>l[-1]:
        l.append(func(c,f,x,i))
        i=i+1
    return l[-2]
fin=open("B-small-attempt0.in")
fout=open("B-small-attempt0.out","w")
n=int(fin.readline())
for i in range(n):
    ns=fin.readline().split()
    fout.write("Case #"+str(i+1)+": "+str(g(float(ns[0]),float(ns[1]),float(ns[2])))+"\n")
    print(g(float(ns[0]),float(ns[1]),float(ns[2])))
fin.close()
fout.close()
