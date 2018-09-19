f = open("A-large (1).in",'r')
n=int(f.readline())
fil = open("out1.txt",'w')
for x in range(n):
    l=[]
    m=[]
    standing =0
    l=f.readline().split()
    req=0
    for y in range(int(l[0])+1):
        m.append(int(l[1][y]))
        if standing>=y:
            standing+=m[y]
        else :
            req+=y-standing
            standing+=y-standing+m[y]
    if(x==n-1):
        fil.write("Case #"+str(x+1)+": "+str(req))
    else:
        fil.write("Case #"+str(x+1)+": "+str(req)+"\n")        
fil.close()

