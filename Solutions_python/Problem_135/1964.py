fob = open("micky.in","r")

TestCases = int(fob.readline())
counter = 1
while TestCases !=0:
    AnswerOne = int(fob.readline())
    Arr1 = []
    for row in range(0,4):
            data = []
            data = fob.readline().split()
            for i in range(0,len(data)):
                data[i] = int(data[i])
            Arr1.append(data)

    AnswerTwo = int(fob.readline())
    Arr2 = []
    for row in range(0,4):
        
            data = []
            data = fob.readline().split()
            for i in range(0,len(data)):
            
                data[i] = int(data[i])
            Arr2.append(data)


    check = 0
    for i in range(0,4):
        for j in range(0,4):
            if(Arr1[AnswerOne-1][i]==Arr2[AnswerTwo-1][j]):
                check+=1
                if check == 1:
                    Answer = Arr1[AnswerOne - 1][i]


    if check == 1:
        print("Case #{}: {}".format(counter,Answer))
        counter+=1
        
    elif check == 0:
        print("Case #{}: Volunteer cheated!".format(counter))
        counter+=1

    else:
        print("Case #{}: Bad magician!".format(counter))
        counter+=1

    TestCases-=1    
        
