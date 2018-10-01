import re

def determinePattern(n, m, lawn):

    for i in range(n):
        for j in range(m):
            height = lawn[i][j]

            flag = True
            for k in range(n):
                if lawn[k][j] > height:
                    flag = False
                    break

            if flag is False:
                flag = True
                for l in range(m):
                    if lawn[i][l] > height:
                        return False

    return True

inFileName = input()
outFileName = "result.out"

inFile = open(inFileName, 'r')
outFile = open(outFileName, 'w')

numTest = inFile.readline().strip()

print(numTest)

for i in range(int(numTest)):
    NM = inFile.readline().strip().split(' ')
    print(NM[0], NM[1])

    a = []
    for j in range(int(NM[0])):
        tmp = inFile.readline().strip().split(' ')
        a.append(list(map(int, tmp)))

    flag = determinePattern(int(NM[0]), int(NM[1]), a)


    result = "Case #" + str(i + 1)
    if flag is True:
        result = result + ": YES"
    else:
        result = result + ": NO"
        
    print(result)
    outFile.write(result + "\n")

inFile.close()
outFile.close()
