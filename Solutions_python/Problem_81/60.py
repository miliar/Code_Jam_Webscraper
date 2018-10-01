from fractions import Fraction

f1=open('input.txt')
f2=open('output.txt','w')

t=int(f1.readline())
for T in range(t):
    n=int(f1.readline())
    a=[]
    wp=[]
    owp=[]
    oowp=[]
    buf1=[0]*(n+1)
    buf2=[0]*(n+1)
    for i in range(n):
        a.append(f1.readline())
    for i in range(n):
        for j in range(n):
            if a[i][j]!='.':
                buf1[i]+=1
                if a[i][j]=='1': buf2[i]+=1
        wp.append(Fraction(buf2[i],buf1[i]))
    for i in range(n):
        s=0
        for j in range(n):
            if a[i][j]=='0':
                s+=Fraction(buf2[j]-1,buf1[j]-1)
            elif a[i][j]=='1':
                s+=Fraction(buf2[j],buf1[j]-1)
        owp.append(s/Fraction(buf1[i],1))
    for i in range(n):
        total=0
        s=0
        for j in range(n):
            if a[i][j]!='.':
                total+=1
                s+=owp[j]
        oowp.append(s/Fraction(total,1))
    
    f2.write('Case #%d:\n'%(T+1))
    for i in range(n):
        f2.write(str(0.25*wp[i]+0.5*owp[i]+0.25*oowp[i])+'\n')

f1.close()
f2.close()
