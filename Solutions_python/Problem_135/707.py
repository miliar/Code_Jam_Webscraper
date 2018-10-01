source="C:\Users\Mani\Desktop\cj\A-small-attempt0.in"
dest="C:\Users\Mani\Desktop\cj\Output.txt"
fin=open(source)
fout=open(dest,'w')
t=int(fin.readline())
for i in range(t):
    
    a=[]
    b=[]
    c=int(fin.readline())
    for j in range(4):
        p=fin.readline()
        p=p.split(" ")
        p=map(int,p)
        a.append(p)

    d=int(fin.readline())
    for j in range(4):
        p=fin.readline()
        p=p.split(" ")
        p=map(int,p)
        b.append(p)

    common=[k for k in a[c-1] if k in b[d-1]]
    if len(common)==1:
        ans=common[0]
        ans=str(ans)
    elif len(common)>1:
        ans="Bad magician!"
    elif len(common)==0:
        ans="Volunteer cheated!"


    fout.write("Case #"+str(i+1)+": "+ans+"\n")

fin.close()
fout.close()
