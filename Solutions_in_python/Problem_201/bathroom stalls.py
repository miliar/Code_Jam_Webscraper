import math
def count(a):
    i=0
    maxx=0
    maxx
    while(i<len(a)-1):
        if(a[i]==1):
            c=0
            q=i
            while(a[i+1]!=1 and i<len(a)-1):
                i=i+1
                c=c+1

            i=i+1
        if(c>maxx):
            maxx=c
            maxx_i=q
            maxx_i2=min(len(a),i)
    return [maxx,maxx_i,maxx_i2]

t = int(input().strip())
for ti in range(t):
    n,k = map(int,input().strip().split(' '))
    b=[]
    for i in range(n+2):
        b.append(0)
    b[0]=1
    b[n+1]=1
    for i in range(k):
        p = count(b)
        q = math.floor((p[1]+p[2])/2)
        b[q]=1
    ls=abs(q-p[1])-1
    rs=abs(q-p[2])-1
    print("Case #",ti+1,": ",max(ls,rs)," ",min(ls,rs),sep='')
