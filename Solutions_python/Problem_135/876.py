f=open("A-small-attempt0.in","r")
out=open("1.txt","w")
T=int(f.readline())
for i in range(T):
    a1=int(f.readline())
    b1=""
    for j in range(4):
        s=f.readline().replace("\n","")
        if j==a1-1:
            b1=s
    a2=int(f.readline())
    b2=""
    for j in range(4):
        s=f.readline().replace("\n","")
        if j==a2-1:
            b2=s
    r1=str.split(b1," ")
    r3=list(r1)
    r2=str.split(b2," ")
    r3.extend(r2)
    ans=[] 
    for n in r3:
        if n in r1 and n in r2:
            if ans.count(n)==0:
                ans.append(n)
                
    if len(ans)==1:
        out.write("Case #"+str(i+1)+": "+ans[0]+"\n")
    elif len(ans)==0:
        out.write("Case #"+str(i+1)+": "+"Volunteer cheated!\n")
    else:
        out.write("Case #"+str(i+1)+": "+"Bad magician!\n")
    
        
    