def fn(a,b,n):
    i=j=cnt=0
    while i<n:
        if a[i]>b[j]:
            cnt+=1
            i+=1
            j+=1
        else:
            i+=1
    return cnt

def fn1(a,b,n):
    i=j=cnt=0
    while j<n:
        if b[j]>a[i]:
            cnt+=1
            i+=1
            j+=1
        else:
            j+=1
    return n-cnt

for cnt in range(input()):
    print "Case #"+`(cnt+1)`+":",
    n=input()
    a=list(float(i)for i in raw_input().split(' '))
    b=list(float(i)for i in raw_input().split(' '))
    a.sort()
    b.sort()
    print `fn(a,b,n)`+" "+`fn1(a,b,n)`
