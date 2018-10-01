file=open("A-small-attempt1.in","r")

cases=int(file.readline()[:-1])
for z in range(cases):
    firstNumber=int(file.readline()[:-1])
    cardsFirst=[]
    for x in range(4):
        cardsFirst.append(file.readline()[:-1].split())



    secondNumber=int(file.readline()[:-1])
    cardsSecond=[]

    for y in range(4):
        cardsSecond.append(file.readline()[:-1].split())


    ChoiceOne=cardsFirst[firstNumber-1]
    ChoiceTwo=cardsSecond[secondNumber-1]

    answers=[]
    count=0
    for x in ChoiceOne:
        if x in ChoiceTwo:
            answers.append(x)
            count+=1

    if(count==1):
        print("Case #"+str(z+1)+": "+answers[0])
    elif(count>1):
        print("Case #"+str(z+1)+": "+"Bad magician!")
    else:
        print("Case #"+str(z+1)+": "+"Volunteer cheated!")
    
        
