import utils


if __name__ == "__main__":
    inputFile = "D-large.in"
    outputFile = "outputQ4Large"
    inputData = utils.createReadFile(inputFile)
    outputData = utils.createWriteFile(outputFile)
    cases = inputData.next()
    cases = cases.replace("\n","")
    print cases
    for index in range(1, int(cases) + 1):
        dWarPoint = 0
        N = int(inputData.next())
        Naomi = inputData.next()
        Naomi = Naomi.replace("\n","")
        Naomi = map(float, Naomi.split(" "))#Naomi.split(" ")
        Naomi = sorted(Naomi)
        Ken = inputData.next()
        Ken = Ken.replace("\n","")
        Ken = map(float, Ken.split(" "))
        Ken = sorted(Ken)
        #print Ken
        #print Naomi

        dWar = 0
        war = 0
        

        dictKen = {value:'k' for value in Ken}
        dictNaomi = {value:'n' for value in Naomi}

        totalList = Ken + Naomi
        totalList = sorted(totalList)
        totalDict = {}
        for indexi in range(len(totalList)):
            totalDict[totalList[indexi]] = indexi
#        totalDict = {value:index for value in totalList}
        #print dictKen, dictNaomi, totalDict
         
        #war
        totalListReverse = reversed(totalList)
        #print totalListReverse
        winToken = 0
        winPoint = 0
        for value in totalListReverse:
            if value in dictKen:
                belonged = 'k'
                winToken += 1
            else:
                belonged = 'n'
                if winToken > 0:
                    winPoint += 1
                    winToken -= 1
        
        warPoint = N - winPoint
#        print warPoint

        #dWar
        totalListReverse = reversed(totalList)
        #print totalListReverse
        winToken = 0
        winPoint = 0
        for value in totalListReverse:
            if value in dictNaomi:
                belonged = 'n'
                winToken += 1
            else:
                belonged = 'k'
                if winToken > 0:
                    winPoint += 1
                    winToken -= 1
        
        dWarPoint = winPoint

                    
        outputString = "Case #" + str(index)+ ": " + str(dWarPoint) + " " + str(warPoint)
        print outputString
        outputData.write(outputString+"\n")
                
            



