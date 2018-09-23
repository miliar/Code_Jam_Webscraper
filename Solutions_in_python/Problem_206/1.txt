# Code by S Vinu Sankar for google codejam
t=int(input())
ans=''
for test in range(1,t+1):
    d,n=list(map(int,input().split()))
    k,s=[],[]
    t=0
    for i in range(n):
        a,b=list(map(int,input().split()))
        if t<(d-a)/b:
            t=(d-a)/b
    ans+='Case #'+str(test)+': %.6f\n' % (d/t)
print(ans)