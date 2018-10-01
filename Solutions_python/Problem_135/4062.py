
f = open('Inputd.in', 'r')
g= open('Outputd.in','w')
cases = int(f.readline())


for i in range(cases):
    rij1=int(f.readline())
    if rij1==1:
        reeks1=f.readline().split()
        f.readline()
        f.readline()
        f.readline()
    elif rij1==2:
        f.readline()
        reeks1=f.readline().split()
        f.readline()
        f.readline()
    elif rij1==3:
        f.readline()
        f.readline()
        reeks1=f.readline().split()
        f.readline()
    elif rij1==4:
        f.readline()
        f.readline()
        f.readline()
        reeks1=f.readline().split()

    rij2=int(f.readline())
    if rij2==1:
        reeks2=f.readline().split()
        f.readline()
        f.readline()
        f.readline()
    elif rij2==2:
        f.readline()
        reeks2=f.readline().split()
        f.readline()
        f.readline()
    elif rij2==3:
        f.readline()
        f.readline()
        reeks2=f.readline().split()
        f.readline()
    elif rij2==4:
        f.readline()
        f.readline()
        f.readline()
        reeks2=f.readline().split()

    number=0
    getal=None
    for j in range(len(reeks1)):
        for k in range(len(reeks1)):
            if reeks1[j]==reeks2[k]:
                number+=1
                getal=reeks1[j]
    if number==0:
        Output="Volunteer cheated!"
    elif number==1:
        Output=getal
    else:
        Output="Bad magician!"


    g.write("Case #"+str(i+1)+": "+Output+"\n")
    
g.close()
f.close()
