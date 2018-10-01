f = open('A-small-attempt0.in','r')
o = open('magician.out','w')

x = int(f.readline())

for c in range(x):
    row1 = int(f.readline())
    mat1=[]
    for i in range(4):
        mat1+=[f.readline()]
    set1 = set(mat1[row1-1].split())
    
    row2 = int(f.readline())
    mat2=[]
    for i in range(4):
        mat2+=[f.readline()]
        
    set2 = set(mat2[row2-1].split())
    isct = set1.intersection(set2)
    if len(isct)==1:
        o.write("Case #"+str(c+1)+": "+str(isct.pop())+"\n")
    elif len(isct)<1:
        o.write("Case #"+str(c+1)+": Volunteer cheated!\n")
    else:
        o.write("Case #"+str(c+1)+": Bad magician!\n")
        
    
f.close()
o.close()
