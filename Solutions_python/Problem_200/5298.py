F1 = open("B-small-attempt2.in","r")
F2 = open("out.out","w")

t = int(F1.readline())  
l = range(t);
for j in range(t):
    l[j]=int(F1.readline())
    
for x in range(t):
    n=l[x]
    for i in range(n+1):
        mystr = str(i)
        flag = 0
        for j in range(len(mystr)-1):
            if int(mystr[j])> int(mystr[j+1]):
                flag=1
        if flag==0:
            num=i
    F2.write("Case #"+str(x+1)+": "+str(num)+"\n")
F2.close()



    


