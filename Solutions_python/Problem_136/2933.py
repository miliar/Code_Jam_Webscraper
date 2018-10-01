f=open('B-large.in','r')
f1=open('B-large.out','a')
n=f.readline()
d=f.readlines()
m=0
for char in d:
    s={}
    s=char.split( )
    c=float(s[0])
    f=float(s[1])
    x=float(s[2])
    r=2
    t=0
    count=0
    while(1):
        if count < c:
            t1=(c-count)/r
            t+=t1
            count=c
        if count == c:
            a=b=r
            z=y=count
            a=r+f
            y=count-c
            t1=x/a
            t2=(x-count)/r
            if(t1 < t2):
                r=r+f
                count-=c
            else:
                t+=t2
                break
    data="Case #%d: %.7f\n"%(m+1,t)
    m+=1
    f1.write(data)
