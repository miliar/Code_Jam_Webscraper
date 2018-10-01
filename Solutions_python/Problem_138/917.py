tc=int(input("TC"))
a=[]
for t in range(tc):
    n=int(input())
    naomi=input()
    naomi=[float(i) for i in naomi.split(" ")]
    naomi.sort()
    ken=input()
    ken=[float(i) for i in ken.split(" ")]
    ken.sort()
    i=0
    j=0
    dv=0
    while(i<n and j<n):
        if(naomi[i]<ken[j]):
            i+=1
        else:
            dv+=1
            i+=1
            j+=1
    i=0
    j=0
    wv=0
    while(i<n and j<n):
        if(ken[i]<naomi[j]):
            i+=1
        else:
            wv+=1
            i+=1
            j+=1
    wv=n-wv
    a.append([dv,wv])
for i in range(len(a)):
    print("Case #"+str(i+1)+": "+str(a[i][0])+" "+str(a[i][1]))
    
