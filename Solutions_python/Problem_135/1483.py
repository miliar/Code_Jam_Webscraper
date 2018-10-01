import re

def MagicTrick(inputFile):
    f = open('MagicTrickOutput.txt', 'w')
    T = int(inputFile.readline())
    i = 1
    while i <= T:
        
        R1 = int(inputFile.readline()) # gives the row number for 1st arrangement
        count = 1
        firstCardDict = {}
        while count <= 4:
            
            row = inputFile.readline() # reads until we get to correct row
            if count == R1:
                firstCardRow = re.split(' |\n', row) # this is row containing the number
                firstCardRow.pop()
                for number in firstCardRow:
                    firstCardDict[number] = None
            
            count += 1
        R2 = int(inputFile.readline())
        count = 1
        
        secondCardDict = {}
        while count <= 4:
            
            row = inputFile.readline()
            if count == R2:
                secondCardRow = re.split(' |\n',row) # this is row containing second number
                secondCardRow.pop()
                for number in secondCardRow:
                    secondCardDict[number] = None
                    
            count += 1
        listOfPossibilities = []
        seenCard = {}

        for card in firstCardDict:
            if card in secondCardDict and card not in seenCard:
                seenCard[card] = None
                listOfPossibilities.append(card)
    
        if len(listOfPossibilities) == 0:
            f.write('Case #' + str(i) + ':' + ' ' + 'Volunteer cheated!' + '\n')
        if len(listOfPossibilities) == 1:
            f.write('Case #' + str(i) + ':' + ' ' + listOfPossibilities[0] + '\n')
        if len(listOfPossibilities) >= 2:
            f.write('Case #' + str(i) + ':' + ' ' + 'Bad magician!' + '\n')
        i += 1
