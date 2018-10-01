f=open('A-small-attempt0.in','r')
cases=int(f.readline())
for x in range (0,cases):
    row1=int(f.readline())

    list1=[]
    
    for i in range(0,4):
        list1.append((f.readline()[:-1]).split(" "))

    row2=int(f.readline()[:-1])
    list2=[]
    for i in range(0,4):
        list2.append((f.readline()[:-1]).split(" "))

    ans=[]
    count=0
    for i in list1[row1-1]:
        if i in list2[row2-1]:
            count+=1
            ans.append(i)

    if (count==1):
        print("case #"+str(x+1)+":"+" "+ans[0])
    elif(count>1):
        print("case #"+str(x+1)+":"+" Bad magician!")
    else:
        print("case #"+str(x+1)+":"+" Volunteer cheated!" )

    
          
          
    
    
    
        
    
