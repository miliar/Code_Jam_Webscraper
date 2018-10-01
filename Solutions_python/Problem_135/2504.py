f1=open("test_magic","r")
f2=open("writ","w")
l = f1.readlines()
for i in range(0,len(l)):
    l[i]=l[i][:-1]
p=1
q=2
list1 = []
list2 = []
for j in range(0,int(l[0])):
    list1 = []
    list2 = []
    x = int(l[p])
    for u in range(0,4):
        g = l[q].split(' ')
        list1.append(g)
        q=q+1
    y = int(l[p+5])
    q = q+1
    for u in range(0,4):
        g = l[q].split(' ')
        list2.append(g)
        q=q+1
    p = p+10
    q = q+1
    count = 0
    for a in list1[x-1]:
            for b in list2[y-1]:
                if(a==b):
                    ans = a
                    count = count + 1
    if(count == 1):
        print "Case #"+str(j+1)+": "+str(ans)
    elif(count>1):
        print "Case #"+str(j+1)+": Bad magician!"
    elif(count == 0):
        print "Case #"+str(j+1)+": Volunteer cheated!"
f1.close