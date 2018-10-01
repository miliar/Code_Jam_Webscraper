fileOpen=open("D-large.in","r+")
fileOpen2=open("dcw.txt","w+")
testCases=int(fileOpen.readline())
for i in range(1,testCases+1):
    logs=int(fileOpen.readline())
    naomi=(fileOpen.readline().split())
    ken=(fileOpen.readline().split())
    naomi=[float(i) for i in naomi]
    ken=[float(i) for i in ken]
    naomi=sorted(naomi)
    ken=sorted(ken)
    naomi2=naomi[:]
    ken2=ken[:]
    pointsNaomiW=0
    pointsNaomiDW=0
    while((len(naomi)>0)&(len(ken)>0)):
        maxNaomi=max(naomi)
        maxKen=max(ken)
        if(maxNaomi>maxKen):
            del naomi[-1]
            del ken[0]
            pointsNaomiW=pointsNaomiW+1
        else:
            lowers=0
            for j in range(0,len(ken)):
                if(ken[j]<maxNaomi):
                    lowers=lowers+1
            del naomi[-1]
            del ken[lowers]
    flag=1
    iterations=0
    while(flag!=0):
        flag=0
        for j in range(0,len(ken2)):
            if(ken2[j]>naomi2[j]):
                flag=flag+1
        if(flag!=0):
            del naomi2[0]
            del ken2[-1]
            iterations=iterations+1
    pointsNaomiDW=logs-iterations
    fileOpen2.write('Case #%d: %d %d\n'%(i,pointsNaomiDW,pointsNaomiW))

    
    
            