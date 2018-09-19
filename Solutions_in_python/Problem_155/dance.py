file=open("E:/q1.in")
ansfile=open("E:/ans01.txt","w")
lines=file.readlines();

noitems=int(lines[0])
l=[]
c=0
ans=0

for i in range (1,noitems+1):
    c=0
    ans=0
    l=list(lines[i].strip("\n").split(" ")[1])
    for j in range(0,len(l)):
        if c<j:
            ans+=j-c
            c=j
        c+=int(l[j])
    ansfile.write("case #"+str(i)+": "+str(ans)+"\n");

file.close()
ansfile.close()

