f=open('Blarge.in','r')
out=open('output.dat','w')

nmax=f.readline()
nmax=int(nmax)

for i in range(nmax):
    s=f.readline()
    s=s.split()
    n=int(s[0])
    sur=int(s[1])
    m=int(s[2])
    sol=0
    for j in range(n):
        p=int(s[3+j])
        if (p==0 and m== 0):
            sol=sol+1
        if (p!=0 and p%3==0):
            if (p/3>=m):
                sol=sol+1
            if (p/3==m-1 and sur>0):
                sur=sur-1
                sol=sol+1
        if (p%3==1):
            if ((p/3 +1) >=m):
                sol=sol+1
        if (p%3==2):
            if (p/3+1 >= m):
                sol=sol +1
            if ((p/3+2)==m and sur>0):
                sur=sur-1
                sol=sol+1
    out.write('Case #')
    out.write(str(i+1))
    out.write(': ')
    out.write(str(sol))
    out.write('\n')
f.close()
out.close()
    
