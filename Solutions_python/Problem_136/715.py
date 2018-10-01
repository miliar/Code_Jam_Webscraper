def commonstart():
    fin=open(r'C:\Users\Administrator\Desktop\google jam\2014\Cookie Clicker Alpha\B-large.in','r')
    fout=open(r'C:\Users\Administrator\Desktop\google jam\2014\Cookie Clicker Alpha\B.out','w')
    return fin,fout
fin,fout=commonstart()
num=int(fin.readline())
for line in range(0,num):
    C,F,X=map(float,fin.readline().split())
    rate=2.0
    time=X/rate
    times=list()
    while time>C/rate+X/(rate+F):
        times.append(C/rate)
        time=X/(rate+F)
        rate+=F
    result=sum(times)+X/rate
    print('Case #%s: %s'%(line+1,result),file=fout)
fin.close()
fout.close()
