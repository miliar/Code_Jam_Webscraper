fil=open('A-large.in','r')
x = fil.readline()
i = 0
p = open('rev.in','w')
while i<int(x):
    mat = []
    nf = 0
    xf=0
    of=0
    rflag=0
    cflag=0
    
    a = 0
    while(a<4):
        rc = []
        y=fil.readline()
        for e in y:
            
            if e=='X':
               rc.append(1)
            elif e=='O':
                rc.append(0)
            elif e=='T':
                rc.append(5)
            elif e=='.':
                nf = 1
                rc.append(10)
        mat.append(rc)
        a+=1
        
    y = fil.readline()
    
    print i+1
    for m in mat:
        print m
    for t in mat:
        if sum(t)==0 or sum(t)==5:
            rflag=1
            of=1
            break
        elif sum(t)==8 or sum(t)==4:
            rflag=1
            xf=1
            break

    if(rflag):
        if xf:
            p.write("Case #"+str(i+1)+": X won\n")
        elif of:
            p.write("Case #"+str(i+1)+": O won\n")
        i+=1
        continue

    a = 0
    while a<4:
        sum1 = mat[1][a] + mat[0][a] + mat[2][a] + mat[3][a]
        if sum1==0 or sum1==5:
            cflag=1
            
            of=1
            break
        elif sum1==8 or sum1==4:
            cflag=1
            xf=1
            break
        a+=1

    if(cflag):
        if xf:
            p.write("Case #"+str(i+1)+": X won\n")
        elif of:
            p.write("Case #"+str(i+1)+": O won\n")
        i+=1
        continue

    sum1 = mat[1][1] + mat[0][0] + mat[2][2] + mat[3][3]
    if sum1==0 or sum1==5:
        p.write("Case #"+str(i+1)+": O won\n")
        i+=1
        continue
    elif sum1==4 or sum1==8:
        p.write("Case #"+str(i+1)+": X won\n")
        i+=1
        continue
    sum1 = mat[0][3] + mat[1][2] + mat[2][1] + mat[3][0]
    if sum1==0 or sum1==5:
        p.write("Case #"+str(i+1)+": O won\n")
        i+=1
        continue
    elif sum1==4 or sum1==8:
        p.write("Case #"+str(i+1)+": X won\n")
        i+=1
        continue

    if nf:
        p.write("Case #"+str(i+1)+": Game has not completed\n")
    else:
        p.write("Case #"+str(i+1)+": Draw\n")

    i+=1
    
p.close()
fil.close()
    
    
    
    
                              
        
