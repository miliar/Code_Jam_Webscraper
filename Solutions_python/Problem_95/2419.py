
def readFromFile(filename):
    inputFile = open(filename, 'r')
    lineArray = []
    for line in inputFile:
        line = line.strip()
        lineArray.append(line)
    inputFile.close()
    return(lineArray)

def writeToFile(filename,listOfLines):
    inputFile = open(filename, 'w')
    for e in listOfLines:
        inputFile.write(e + '\n')
    inputFile.close()

oldLetters = []
newLetters = []
changeLetters = ['y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q']

oldLetters = readFromFile('A-small-attempt1.in')

for i in range(1,int(oldLetters[0])+1):
    newLetters.append([])
    newString = 'Case #' + str(i) + ': '
    for e in range(0,len(oldLetters[i])):
        if (oldLetters[i][e] == ' '):
            newString += ' '
        elif (ord(oldLetters[i][e])-97 < 26):
            newString += (changeLetters[ord(oldLetters[i][e]) - 97])
    newLetters[i-1] = newString

writeToFile('output.txt',newLetters)
