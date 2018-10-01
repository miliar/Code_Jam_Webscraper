import sys


if __name__ == '__main__':
    
    outFP = open(sys.argv[1]+'.out.txt', 'w')

    inputLines = open(sys.argv[1], 'r').read().strip().split('\n')

    L, D, N = map(int, inputLines.pop(0).split())

    treeRoot = dict()

    for i in range(D):
        words = inputLines.pop(0)

        curRoot = treeRoot
        for j in range(L):
            letter = words[j]
            if letter in curRoot:
                curRoot = curRoot[letter]
                continue
            else:
                curRoot[letter] = dict()
                curRoot = curRoot[letter]

    caseNO = 1
    for line in inputLines:
        testLetters = list()
        idx = 0
        enterBrace = False
        for i in range(len(line)):
            if line[i] == '(':
                enterBrace = True
                continue
            elif line[i] == ')':
                enterBrace = False
                idx += 1
            else:
                if len(testLetters) <= idx:
                    testLetters.append(list())
                testLetters[idx].append(line[i])
                if not enterBrace:
                    idx += 1

        def travel(rLetterTree, tLetterGroup, tLetterIdx):
            if tLetterIdx >= L:
                return 1
            correct = 0
            curLetterGroup = tLetterGroup[tLetterIdx]
            for i in range(len(curLetterGroup)):
                curLetter = curLetterGroup[i]
                if curLetter in rLetterTree:
                    correct += travel(rLetterTree[curLetter], tLetterGroup, tLetterIdx + 1)
            return correct

        result = travel(treeRoot, testLetters, 0)

        pLine = 'Case #%i: %i'%(caseNO, result)
        print pLine
        outFP.write(pLine+'\n')
        caseNO += 1




