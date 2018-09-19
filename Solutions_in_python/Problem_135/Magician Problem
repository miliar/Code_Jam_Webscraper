f = open('C:\Python27\A-small-attempt0.in', 'r')
ff =  open('C:\Python27\Magician.txt', 'w')
ip = list(f)

temp3 = ip[0].rsplit()
test = int(temp3[0])
z=1

a = []
b = []
c = []
d = []
for i in range(test):
    temp3 = ip[z].rsplit()
    x=int(temp3[0])
    z+=1
    x-=1
    a=[]
    c=[]
    
    for j in range(4):
        temp2 = ip[z].rsplit()
        b=[]
        for k in range(4):
            temp= int(temp2[k])
            b.append(temp)
        a.append(b)
        z+=1
        
    temp3 = ip[z].rsplit()
    y=int(temp3[0])
    y-=1
    z+=1
    
    for j in range(4):
        temp2 = ip[z].rsplit()
        d=[]
        for k in range(4):
                     
            temp= int(temp2[k])
            d.append(temp)
        c.append(d)
        z+=1
     
    count= 0;
    for j in range(1,17):
        if (j in c[y]) and (j in a[x]):
            count += 1
            res = j
           
    if count == 0:
        print ( ("Case #"+str(i+1) + ": " + "Volunteer cheated!"))
    elif count ==1:
        print ( str("Case #"+str(i+1) + ": " + str(res)))
    elif count>1:
        print ( ("Case #" + str(i+1) + ": " + "Bad magician!"))                