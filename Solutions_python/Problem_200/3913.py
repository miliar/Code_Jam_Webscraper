def isTidy(m):
    e=str(m)
    for i in range(0,len(e)-1):
        if(int(e[i])>int(e[i+1])):
               return 0
    return 1
f = open('B-small-attempt4.in', 'r')
f2 = open('B-small-attempt4-output.out', 'w')
k=0
nn=int(f.readline())
for line in f:
    k=k+1
    if k>nn:
        break
    n=int(line)
    if n<10:
        f2.write("Case #"+str(k)+": "+str(n)+'\n')
    else:
        p=isTidy(n)
        m=n
        while p==0:
            m=(m//10)*10-1
            p=isTidy(m)
        f2.write("Case #"+str(k)+": "+str(m)+'\n')
f.close()
f2.close()
