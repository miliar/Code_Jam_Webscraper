def rev_check(nm):
    st=sorted(str(nm))
    rev=""
    for m in st:
        rev=rev+m
    if int(rev)==nm:
        return True
def cntr(n):
    nm=n
    while(not rev_check(nm)):
        nm=nm-1
    return nm

with open('B-small-attempt2.in') as f:
    lis1 = f.readlines()
lis=[m.strip() for m in lis1[1:len(lis1)]]  
cs=0
f=open('op.txt','w')
for m in lis:
    cs=cs+1
    f.write("Case #"+str(cs)+": "+str(cntr(int(m)))+'\n')
f.close()
