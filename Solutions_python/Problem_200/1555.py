def start(x):
    x=list(x)
    for i in range(len(x)):
        x[i]=int(x[i])
    i=0
    j=1
    while j<len(x):
        if x[i]<=x[j]:
            i+=1
            j+=1
        else:
            x[i]=x[i]-1
            while j<len(x):
                x[j]=9
                j+=1
    while i>0:
        if x[i]<x[i-1]:
            x[i-1]-=1
            x[i]=9
            i-=1
        else:
            break
    for i in range(len(x)):
        x[i]=str(x[i])
    return int("".join(x))


f=open("B-small-attempt0.in.txt",'r')
for i in range(int(f.readline())):
    x=f.readline()

    print "Case #"+str(i+1)+": "+str(start(str(int(x))))
