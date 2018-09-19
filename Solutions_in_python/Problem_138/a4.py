from math import floor
aaa = open("a.txt","r").readlines()
f=open("b.txt","w")
f.write("")
f.close()
def won(a,b):
    if float(a)>float(b):
        return "ken"
def getken(kens,naomi):
    abss={}
    for i in kens:
        abss[i]=float(i)-float(naomi)
    positives={}
    negatives={}
    for i in abss:
        if abss[i]>0:
            positives[i]=abss[i]
        else:
            negatives[i]=abss[i]
    if positives:
        mins=min(positives.values())
        for i in positives:
            if positives[i]==mins:
                return i
    else:
        mins=min(negatives.values())
        for i in negatives:
            if negatives[i]==mins:
                return i
for i in range(0,len(aaa),3):
    print "Case %d" % ((i/3)+1)
    naomis=aaa[i+1].strip().replace("\n","").split(" ")
    kens=aaa[i+2].strip().replace("\n","").split(" ")
    kens2=[]
    for ken in kens:
        kens2.append(float(ken))
    kens3=kens2[:]
    kenscore=0
    naomiscore=0
    for naomi in naomis:
        ken=float(getken(kens2,float(naomi)))
        ww=won(ken,float(naomi))
        kens2.remove(ken)
        if ww=="ken":
            kenscore+=1
        else:
            naomiscore+=1
    ghdg=naomiscore
    kenscore=0
    naomiscore=0
    kens2=kens3[:]
    naomis2=[]
    for j in naomis:
        naomis2.append(float(j))
    naomis2.sort()
    kens3=kens2[:]
    kens3.sort()
    naomis3=naomis2[:]
    for j in range(0,len(kens3)):
        fken=max(kens2)
        fken2=max(kens2)- max(naomis3)
        if fken2>0:
            kenscore+=1
            kens2.remove(max(kens2))
            naomis3.remove(min(naomis3))
        else:
            naomiscore+=1
            kens2.remove(max(kens2))
            naomis3.remove(max(naomis3))
    ghdg2=naomiscore
    f=open("b.txt","a")
    f.write("Case #%d: " % ((i/3)+1)+str(ghdg2)+u" "+str(ghdg)+u"\n")
    f.close()
    
