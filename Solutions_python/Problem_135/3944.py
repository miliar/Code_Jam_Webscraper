ip=open("A-small-attempt1.in","r")
ite=ip.readline()
ite=int(ite)
row1,new1=list(),list()

number=0
result=list()
for cnt in range(ite):
    count=0
    ans1=ip.readline()
    ans1=int(ans1)
    for i in range(1,5):
        x=ip.readline()
        if(i==ans1):
            x=str(x)
            row1=x.split()
    ans2=ip.readline()
    ans2=int(ans2)
    for i in range(1,5):
        x=ip.readline()
        if(i==ans2):
            x=str(x)
            new1=x.split()    
    for i in range(4):
        if(row1[i] in new1):
            number=row1[i]
            count+=1
    if count==0:
        result.append("Volunteer cheated!")
    elif count==1:
        result.append(str(number))
    else:
        result.append("Bad magician!")
ip.close()
out=open("output.txt","w")
for cnt in range(ite):      
    out.write("Case #"+str(cnt+1)+": "+result[cnt]+"\n")
out.close()
