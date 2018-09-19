def buildWord(inWord, inList, inSet):
    #print inWord
    if len(inList) == 0:
        if inWord in inSet:
            return 1
        return 0
    else:
        
        count = 0
        for l in inList[0]:
            for s in inSet:
                if s.find(inWord+l) == 0:
                    count += buildWord(inWord + l, inList[1:len(inList)], inSet)
                    break;
        return count



inFile = open("D:\\gcj\\A-small-attempt1.in", 'r')

lines = [line.rstrip() for line in inFile.readlines()]

setup = lines[0].rstrip("\n").split(" ")

wordLength = int(setup[0])
langWords = int(setup[1])
testCases = int(setup[2])


wordSet = frozenset(lines[1:langWords+1])

tests = lines[(langWords+1):len(lines)]

caseNum = 1
for test in tests:
    tokens = list()
    currentToken = ""
    inToken = False
    for l in test:
        if l == '(':
            inToken = True
        elif l == ')':
            inToken = False
            tokens.append(currentToken)
            currentToken = ""
        elif inToken:
            currentToken += l
        else: 
            tokens.append(l)

    matches = buildWord("", tokens, wordSet)


    print "Case #" + str(caseNum) + ": " + str(matches)
    caseNum = caseNum + 1
    
    
