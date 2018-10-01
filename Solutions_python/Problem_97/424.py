f = file("test.in",'r')
lines = f.readlines()
f.close()

n = int(lines[0])
ans = []
for i in range(1,n+1) :
    a = int(lines[i].split(' ')[0])
    b = int(lines[i].split(' ')[1])
    count = 0
    for j in range(a,b+1) :
        recylist = []
        l = len(str(j))
        for k in range(1,l) :
            p1 = j/pow(10,k)
            p2 = j%pow(10,k)
            recyj = p2*pow(10,l-k)+p1
            if recyj <= b :
               if recyj>=a :
                  if j < recyj :
                     t = j, recyj
                     if t not in recylist :
                        recylist.append(t)
                        count+=1
    ans.append(count)
    print "Case #"+str(i)+": "+str(count)






