def makeNum(n):
    t=0
    for i in range(len(n)):
        t=t*10+n[i]
    return t

def makeList(x):
    lis = list(str(x))
    lis = [int(i) for i in lis]
    return lis

def check(n):
    l=makeList(n)
    for i in range(len(l)-1,0,-1):
        if(l[i]<l[i-1]):
            for j in range(i,len(l)):
                l[j]=0
            #print(makeNum(l)-1)
            l=makeList(makeNum(l)-1)
            i=0
    return makeNum(l)

t=int(input())
f=open('/home/shubham/python_scripts/output.txt',"w")
for k in range(t):
    n=int(input())
    ans=check(n)
    f.write("Case #%d: %d\n"%(k+1,ans))



