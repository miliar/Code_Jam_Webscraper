def sta(x,y):
    if y==1:
        val=x
        if val%2==0:
            return [(val/2),(val/2)-1]
        else:
            return [(val-1)/2,(val-1)/2]

    x1=x
    a=1
    sum=a
    while sum<y:
        if x%2==0:
            x=(x/2)
        elif x%2==1:
            x=(x-1)/2
        a=a*2
        sum += a
        if sum>=y:
            sum=sum-a
            a=a/2
            break
    b=(x*a*2)-(x1-sum)
    high=(a*2)-b
    low=b
    val=x

    if (y-sum)-high<=0:
        if val%2==0:
            return [(val/2),(val/2)-1]
        else:
            return [(val-1)/2,(val-1)/2]
    elif y-sum-high>0:
        val=val-1
        if (val)%2==0:
            return [(val/2),(val/2)-1]
        else:
            return [(val-1)/2,(val-1)/2]


f=open("C-small-1-attempt01.in.txt",'r')
for i in range(int(f.readline())):
    x=f.readline().split(" ")
    r=sta(int(x[0]),int(x[1]))
    print "Case #"+str(i+1)+": "+str(r[0])+" "+str(r[1])

