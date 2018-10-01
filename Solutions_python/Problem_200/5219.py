def istidy(n):
    n=str(n)
    f=0
    for i in range(len(n)-1):
        if n[i]>n[i+1]:
            f=1
    if f ==1:
        return 0
    else:
        return 1

A=int(raw_input(""))
L=[]
for i in range(A):
    n=int(raw_input(""))
    if n<10:
        L.append(n)
    else:
        j=n
        while j>10:
            if istidy(j):
                L.append(j)
                break
            else:
                j-=1
for k in xrange(len(L)):
    a="Case #"
    b=":"
    c=a+str(k+1)+b+" "+str(L[k])
    print c
    
    
