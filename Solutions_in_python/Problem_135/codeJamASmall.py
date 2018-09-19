from fileModder import *
def main():
    fileName = raw_input("FileName: ")
    inputReader = open(fileName,"r")
    myInput = inputReader.readlines()
    myInput = killNL(myInput)
    #print myInput
    lineCounter = 0
    runs = int(myInput[lineCounter])
    lineCounter +=1
    answers = []
    for k in range(runs):
        #print lineCounter
        firstRow = int(myInput[lineCounter])
        lineCounter +=1
        possibleNums = []
        for i in range(4):
            if i == (firstRow-1):
                possibleNums = myInput[lineCounter].split()
                lineCounter +=1
            else:
                lineCounter +=1
        secondRow = int(myInput[lineCounter])
        lineCounter +=1
        finalNums = []
        for i in range(4):
            if i == (secondRow-1):
                for j in myInput[lineCounter].split():
                    for l in possibleNums:
                        if j == l:
                            finalNums.append(j)
                lineCounter +=1
            else:
                lineCounter +=1
        if len(finalNums) == 1:
            answers.append("Case #" + str((k+1))+": "+finalNums[0])
        elif len(finalNums) == 0:
            answers.append("Case #" + str((k+1))+": "+"Volunteer cheated!")
        else:
            answers.append("Case #" + str((k+1))+": "+"Bad magician!")
    output = open("magicianOutput.txt","w")
    for k in answers:
        output.write(k + "\n")
    output.close()
main()
