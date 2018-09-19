andar=open("input.in","r")
bahar=open("output.txt","w")
a=int(andar.readline())
c=[]
summe=0
counter1=1
while(a):
    ans=0
    a=a-1
    ans=0
    b=andar.readline()
    b=b.split()
    c=andar.readline()
    c=c.split()
    for i in range(len(b)):
        b[i]=int(b[i])
    for i in range(len(c)):
        c[i]=int(c[i])
    runs=b[0]
    maxp=b[1]
    grps=b[2]
    if(a==29):
        print c," ",maxp
    while(runs):
        summe=0
        counter=0
        runs=runs-1
        for counter in range(len(c)):
            if(summe<maxp):
                summe=summe+c[counter]
                if(summe>maxp):
                    summe=summe-c[counter]
                    temp=c[:counter]
                    while(counter):
                        counter=counter-1
                        c.pop(0)
                    c=c+temp
                    break
                if(summe==maxp):
                    counter=counter+1
                    temp=c[:counter]
                    while(counter):
                        counter=counter-1
                        c.pop(0)
                    c=c+temp
                    break
        ans=ans+summe
        if(a==29):
            print runs," ",c," ",summe," ",temp
    s="Case #"+str(counter1)+": "+str(ans)+"\n"
    bahar.write(s)
    counter1=counter1+1
    if(a==29):
        print ans
