def readFile(fileName):
    f = open(fileName)
    gameList = []
    for line in f:
        content = line.split()
        if len(content) == 1:
            print content[0],'test cases are read.'
        else:
            X = int(content[0])
            R = int(content[1])
            C = int(content[2])
            gameList.append((X,R,C))
    f.close()
    return gameList

def whoWin(X,R,C):
    if X == 1:
        return 'GABRIEL'
    elif X == 2 and (R*C) % X == 0:
        return 'GABRIEL'
    elif X == 3 and (R*C) % X == 0 and (R*C) > 4:
        return 'GABRIEL'
    elif X == 4 and (R*C) % X == 0 and (R*C) > 8:
        return 'GABRIEL'
    return 'RICHARD'

def solveIt(gameList):
    output = ''
    for j in range(len(gameList)):
        game = gameList[j]
        winner = whoWin(game[0],game[1],game[2])
        output +=  'Case #{0}: {1}\n'.format(j+1,winner)
    return output[:-1]

def writeOutput(fileName,output):
    f = open(fileName, 'w')
    f.write(output)

##inputFile = 'Dtest.txt'
##outputFile = 'test_output.txt'

inputFile = 'D.txt'
outputFile = 'D_output.txt'

##inputFile = 'Db.txt'
##outputFile = 'Db_output.txt'

gameList = readFile(inputFile)
output = solveIt(gameList)
writeOutput(outputFile,output)
print 'Done!'
