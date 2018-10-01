
fi= open("C:\\ASD\\A.in", 'r')
fo= open("C:\\ASD\\A.out", 'w')
xn=int(fi.readline().rstrip())

for xj in range(xn):
    a=fi.readline().rstrip()
    b={}
    i=0
    for j in a:
        if not j in b:
            b[j]=i
            i=i+1

    for i in b:
        if b[i]==0:
            b[i]=1
        elif b[i]==1:
                b[i]=0

    n=len(b)
    num=0
    for i,j in enumerate(a[::-1]):
        num=num+b[j]*pow(n,i)
        
    fo.write("Case #"+str(xj+1)+": "+str(num)+"\n")