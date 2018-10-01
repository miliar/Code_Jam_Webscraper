test=input()
for t in range(1,test+1):
    countdw=0
    countw=0
    temp=0
    n=input()
    if(n==1):
        naomi=input()
        ken=input()
        if(naomi > ken):
            countw = 1
            countdw =1
    else:
        s=raw_input()
        naomi=s.split()
        naomi=map(float,naomi)
        s=raw_input()
        ken=s.split()
        ken=map(float,ken)
        naomi=sorted(naomi)
        ken=sorted(ken)
        naomi2=list(naomi)
        ken2=list(ken)
        for i in range(0,n):
            if(naomi[0] > ken[0]):
                countdw+=1
                naomi.remove(naomi[0])
                ken.remove(ken[0])
                temp+=1
            else:
                naomi.remove(naomi[0])
                ken.remove(ken[n-1-temp])
                temp+=1
        temp=0
        for i in range(0,n):
            if(naomi2[n-1-temp]>ken2[n-1-temp]):
                countw+=1
                naomi2.remove(naomi2[n-1-temp])
                ken2.remove(ken2[0])
                temp+=1
            else:
                naomi2.remove(naomi2[n-1-temp])
                ken2.remove(ken2[n-1-temp])
                temp+=1
    print "Case #"+str(t)+": "+str(countdw)+" "+str(countw)
