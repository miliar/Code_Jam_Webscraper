__author__ = 'majid'
import copy
def delta(l,n):
    return [i for i in l if i>n]
def func1(al,bl):
    a=copy.deepcopy(al)
    b=copy.deepcopy(bl)
    a.sort()
    b.sort()
    s=0
    n=len(a)
    for i in range(n):
        t=delta(b,a[0])
        if t:
            s=s+1
        else:
            break
        a.pop(0)
        b.remove(t.pop(0))
    return n-s
def func2(al,bl):
    a=copy.deepcopy(al)
    b=copy.deepcopy(bl)
    a.sort()
    b.sort()
    s=0
    n=len(a)
    for i in range(n):
        x=a.pop(0)
        y=b.pop(0)
        if x>y:
            s=s+1
        else:
            b.append(y)
            b.sort()
            b.pop(-1)
    return s
fin=open("D-small-attempt0.in")
fout=open("D-small-attempt0.out","w")
n=int(fin.readline())
for i in range(n):
    fin.readline()
    a=[float(i) for i in fin.readline().split()]
    b=[float(i) for i in fin.readline().split()]
    st="Case #"+str(i+1)+": "+str(func2(a,b))+" "+str(func1(a,b))+"\n"
    fout.write(st)
    print(st)
fin.close()
fout.close()