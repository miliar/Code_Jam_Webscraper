f=open("C:\Users\Prateek Saraswat\Downloads\A-small-attempt1 (1).in")
NoTestCases=int(f.readline())
PrintAns=[]
#(NoTestCases+1)
for i in range(1,NoTestCases+1):
    firstAnswerRow=int(f.readline())
    
    FirstTable=[]
    for j in range(4):
        
       Row=list(f.readline().split())
       FirstTable.append(Row)
    
    secondAnswerRow=int(f.readline())
    
    SecondTable=[]
    for j in range(4):
        
       Rows=list(f.readline().split())
       SecondTable.append(Rows)
   
    RowOne=FirstTable[firstAnswerRow-1]
    RowTwo=SecondTable[secondAnswerRow-1]
    #print RowOne
    #print RowTwo
    count=0
    num=0
    for k in RowOne:
        if (k in RowTwo):
            num=int(k)
            #print num
            count+=1
            #print 'Count-'+str(count)
            if count>1:
                break
    if count==1:
        s= 'Case #'+str(i)+': '+str(num)        
        PrintAns.append(s)
    elif count>1:
        s= 'Case #'+str(i)+': Bad magician!'
        PrintAns.append(s)
    else:
        s= 'Case #'+str(i)+': Volunteer cheated!'
        PrintAns.append(s)
o=open('C:\Users\Prateek Saraswat\Downloads\output2','a')
for s in PrintAns:
    o.write(s+'\n')
o.close()
    
    