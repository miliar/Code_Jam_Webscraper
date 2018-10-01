inFile = open('A-large.in')
outFile = open('A-large.out', 'w')
testCases = int(inFile.readline())
caseNo = 1
while caseNo <= testCases:
    case = inFile.readline()
    flipperSize = int(case[case.index(' '):])
    pancakes = [True]*case.index(' ')
    for i in range(case.index(' ')):
        if case[i]== '-':
            pancakes[i] = False
    flips = 0
    print('Case %s' % (caseNo))
    print(pancakes)
    for position in  range(len(pancakes)-flipperSize+1):
        if not pancakes[position]:
            flips += 1
            for i in range(flipperSize):
                pancakes[position+i] = not pancakes[position+i]
            print(pancakes)
    if False in pancakes[len(pancakes)-flipperSize+1:]:
        outFile.write('Case #%s: %s\n' % (caseNo,'IMPOSSIBLE'))
        print('IMPOSSIBLE')
    else:
        outFile.write('Case #%s: %s\n' % (caseNo,flips))
        print('%s flips' % (flips))
    caseNo += 1
inFile.close()
outFile.close()