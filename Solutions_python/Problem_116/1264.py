from goto import goto, comefrom, label
finn=open('C:/Users/HP/Desktop/input.txt','r')
fout=open('C:/Users/HP/Desktop/output.txt','w')
t1=finn.readline()
k1=int(t1)
for j in range(0, k1):
    a=[]
    a.append(finn.readline())    
    a.append(finn.readline())
    a.append(finn.readline())
    a.append(finn.readline())
    c1=[]
    c1.append(a[0][0])
    c1.append(a[1][0])
    c1.append(a[2][0])
    c1.append(a[3][0])
    a.append(c1)
    c1=[]
    c1.append(a[0][1])
    c1.append(a[1][1])
    c1.append(a[2][1])
    c1.append(a[3][1])
    a.append(c1)
    c1=[]
    c1.append(a[0][2])
    c1.append(a[1][2])
    c1.append(a[2][2])
    c1.append(a[3][2])
    a.append(c1)
    c1=[]
    c1.append(a[0][3])
    c1.append(a[1][3])
    c1.append(a[2][3])
    c1.append(a[3][3])
    a.append(c1)
    c1=[]
    c1.append(a[0][0])
    c1.append(a[1][1])
    c1.append(a[2][2])
    c1.append(a[3][3])
    a.append(c1)
    c1=[]
    c1.append(a[0][3])
    c1.append(a[1][2])
    c1.append(a[2][1])
    c1.append(a[3][0])
    a.append(c1)
    chk=0
    for i in range(10):
        if(a[i].count('X')==4)or((a[i].count('X')==3)and(a[i].count('T')==1)):
            fout.write('Case #'+str(j+1)+': X won\n')
            goto .end
        if(a[i].count('O')==4)or((a[i].count('O')==3)and(a[i].count('T')==1)):
            fout.write('Case #'+str(j+1)+': O won\n')
            goto .end
        if(a[i].count('.')!=0):
            chk=1
    if(chk==1):
        fout.write('Case #'+str(j+1)+': Game has not completed\n')
    else:
        fout.write('Case #'+str(j+1)+': Draw\n')
    label .end
    finn.readline()
finn.close()
fout.close()
