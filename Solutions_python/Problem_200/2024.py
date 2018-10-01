t = int(input())


for j in range(t):
    nn = int(input())
    n = list(str(nn))

    l = len(n)
    i = 0
    while(i<l-1):
        if n[i]>n[i+1]:
            n[i]=str(int(n[i])-1)
            n[i+1:]=['9']*(l-i-1)
            if i>0:
                i=i-1
        else:
            i+=1

    print "Case #%d:"%(j+1),int("".join(x for x in n))
