f=open("D-large.in","r")
out=open("1.out","w")
T=int(f.readline())
for k in range(T):
    n=int(f.readline())
    naomi=f.readline().replace("\n","").split(" ")
    naomi.sort()
    ken=f.readline().replace("\n","").split(" ")
    ken.sort()
    i=0
    j=0
    s1=0
    while(i<n and j<n):
        if naomi[i]<ken[j]:
            i+=1
        else:
            s1+=1
            i+=1
            j+=1
    i=0
    j=0
    count=0
    while(j<n and i<n):
        if naomi[i]>ken[j]:
            j+=1
        else:
            i+=1
            j+=1
            count+=1
    s2=n-count
    ret ="Case #"+str(k+1)+": "+str(s1)+" "+str(s2)+"\n"
    print ret
    out.write(ret)
        