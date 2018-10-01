file_1= open("y.txt","r")
a0= int(file_1.readline().rstrip())

p=1

while(p<=a0):
    a1= int(file_1.readline().rstrip())
    array=[]
    array2=[]

    for line in file_1:
        b=line.split()
        array.append(b)
        if len(array)==4:
            break
   
    a2= int(file_1.readline().rstrip())


    for line in file_1:
        b=line.split()
        array2.append(b)
        if len(array2)==4:
            break


    c=array[a1-1]
    d=array2[a2-1]

    stack=[]
    for x in range(0,4):
        q=c[x]

        for x2 in range(0,4):
            q2=d[x2]
            if q==q2:
                stack.append(q2)        

        
    if len(stack)==0:
        print("Case #"+ str(p) +": Volunteer Cheated!")
    elif len(stack)>1:
        print("Case #"+str(p)+ ": Bad magician!")
    else:
        print("Case #"+str(p)+": "+stack[0])

    p+=1
