import sys

def getIfPossibleUnsurprising(score, maxScore):
    print ("Score is: " + str(score) + " " + "max is:" + str(maxScore))
    if maxScore == 0:
        return True
    if int(score) == 0:
        return False
    return True if (int(score) >= int(maxScore*3 - 2)) else False

def getIfPossibleSurprising(score, maxScore):
    if int(score) == 0:
        return False
    return True if (int(score) >= int(maxScore*3 - 4)) else False

def parseMessage(message):
    information = message.split()
    numberOfDancers = int(information[0])
    surprisingScores = int(information[1])
    maximumScore = int(information[2])
    dancerScores = information[3:]
    print(str(dancerScores))
    return (numberOfDancers, surprisingScores, maximumScore, dancerScores)

def getNumberPossible(dScores, maxScore, sScores):
    #dScores is the list of dancer scores;
    #sScores is the number of surprising scores
    numberPossible =0
    print ("Number of surprises is: " + str(sScores))
    for x in dScores:
        if getIfPossibleUnsurprising(x, maxScore):
            print("herp")
            numberPossible += 1
        elif sScores >= 1 and getIfPossibleSurprising(x, maxScore):
            print("supplies!")
            numberPossible += 1
            sScores -= 1
            print("The number of surprises left is: " + str(sScores))
    return numberPossible

def main():
    filename = input()
    fileStream = open(filename)
    message = fileStream.readlines()
    out = open("outFile5.out", 'w')
    for x in range(1, int(message[0])+1):
        numDancers, sScores, maxScore, dScores = parseMessage(message[x])
        case = "Case #" + str(x) + ": " + \
            str(getNumberPossible(dScores, maxScore, sScores)) + '\n'
        print(case)
        out.write(case)
    out.close
        
if __name__ == "__main__":
    main()
    
