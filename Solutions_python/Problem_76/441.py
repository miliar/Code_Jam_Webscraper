myfile=open("C-large.in", "r")
inp=myfile.read().split("\n")

def sub(tA,tB):
    if len(tA)>len(tB): leng=len(tA)
    else: leng=len(tB)
    tA=tA[::-1]
    tB=tB[::-1]
    s=""
    for q in range(leng):
        try: o=int(tA[q])
        except: o=0
        try: p=int(tB[q])
        except: p=0
        o=o-p
        if o<0: o*=-1
        s=str(o)+s[:]
    return s

def add(tA,tB):
    if len(tA)>len(tB): leng=len(tA)
    else: leng=len(tB)
    tA=tA[::-1]
    tB=tB[::-1]
    s=""
    for q in range(leng):
        try: o=int(tA[q])
        except: o=0
        try: p=int(tB[q])
        except: p=0
        o=o+p
        if o==2: o=0
        s=str(o)+s[:]
    return s

def bina(num):
    s=""
    while True:
        re=str(num%2)
        s=re+s

        num-=int(re)
        
        if num==0: break
        num/=2

    return s

def pr(newlist):
    newlist.sort()

    s="0"
    for x in newlist[1:]:
        s=add(s,x)

    while True:
        if s[0]=="0":
            s=s[1:]
        else:
            break
    if s!=newlist[0]:
        print" fail"
    else:
        print s
        print newlist[0]
fullanswer=""
i=0
for casenumber in range(int(inp[0])):
    answer=""
    even=[]
    i+=1
    hm=int(inp[i])
    i+=1
    numbers=inp[i].split(" ")
    newlist=[]
    for x in numbers:
        newlist.append(bina(int(x)))
    for x in newlist:
        e=0
        for y in x[::-1]:
            try: even[e]+=int(y)
            except:
                even.append([])
                even[e]=int(y)
            e+=1

    obj=[]

    for x in even:
        obj.append(x/2)
        if x%2!=0:
            answer="NO"
            
    if answer!="NO":
        num=[]
        for x in numbers:
            num.append(int(x))
        num.sort()
        
        answer=sum(num[1:])
        answer=str(answer)

    fullanswer+="Case #%d: %s\n" % (casenumber+1,answer)

results=open("C.out","w")
results.write(fullanswer)
myfile.close()
results.close()
