
file = open("text.txt")


testCases = int(file.readline())

for tNum in range(1,testCases+1):
    firstNumGuess = int(file.readline())
    
    listOne  = []
    Seclist  = [] 
    for i in range(4):
        listOne.append(file.readline().split())
        
    
    firstList = listOne[firstNumGuess-1]

    
    
    secondNumGuess = int(file.readline())
    
    for i in range(4):
        Seclist.append(file.readline().split())
        
    secondList = Seclist[secondNumGuess -1]
    
    count = 0
    magicNumber =-1
    
    for x in secondList:
        if x in firstList:
            magicNumber = x
            count +=1
            
            
    if count == 1:
        print ("Case #{}: {}".format(tNum,magicNumber))
    elif count > 1:
        print("Case #{}: Bad magician!".format(tNum))
    else:
        print("Case #{}: Volunteer cheated!".format(tNum))
        
    



