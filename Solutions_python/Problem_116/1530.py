f = open('A-small-attempt1.in')
lines = f.readlines()
f.close()
line = []
for element in lines:
    line.append(element.replace('\n', ''))

num = int(line[0])
line.pop(0)
lines = []
temp = []
i = 1
for element in line:
    if element == '':
        continue
    temp.append(element)
    i += 1
    if i == 5:
        i = 1
        lines.append(temp)
        temp = []
f = open('output.txt', 'w')
answerFound = False
countX = 0
countO = 0
caseNumber = 0
for case in lines:
    caseNumber += 1
    for element in case:
        if element.count('X') + element.count('T') == 4:
            win = 'X'
            f.writelines('Case #' + str(caseNumber) + ': ' + win + ' won\n')
            answerFound = True
            break
        elif element.count('O') + element.count('T') == 4:
            win = 'O'
            f.writelines('Case #' + str(caseNumber) + ': ' + win + ' won\n')
            answerFound = True
            break
    if answerFound == False:
        for i in range(4):
            for j in range(4):
                if case[j][i] == 'X' or case[j][i] == 'T':
                    countX += 1
                if case[j][i] == 'O' or case[j][i] == 'T':
                    countO += 1
                if countX == 4:
                    win = 'X'
                    f.writelines('Case #' + str(caseNumber) + ': ' + win + ' won\n')
                    answerFound = True
                    break
                elif countO == 4:
                    win = 'O'
                    f.writelines('Case #' + str(caseNumber) + ': ' + win + ' won\n')
                    answerFound = True
                    break
            countX = 0
            countO = 0
        #sleva napravo
        i = 0
        for element in case:
            if element[i] == 'X':
                countX += 1
            elif element[i] == 'O':
                countO += 1
            elif element[i] == 'T':
                countO += 1
                countX += 1
            i += 1
        if countX == 4:
            countX = 0
            win = 'X'
            f.writelines('Case #' + str(caseNumber) + ': ' + win + ' won\n')
            answerFound = True
        elif countO == 4:
            countO = 0
            win = 'O'
            f.writelines('Case #' + str(caseNumber) + ': ' + win + ' won\n')
            answerFound = True
        else:
            countX = 0
            countO = 0
        #sprava nalevo
        i = 0
        for element in case:
            if element[len(element)-i-1] == 'X':
                countX += 1
            elif element[len(element)-i-1] == 'O':
                countO += 1
            elif element[len(element)-i-1] == 'T':
                countO += 1
                countX += 1
            i += 1
        if countX == 4:
            countX = 0
            win = 'X'
            f.writelines('Case #' + str(caseNumber) + ': ' + win + ' won\n')
            answerFound = True
        elif countO == 4:
            countO = 0
            win = 'O'
            f.writelines('Case #' + str(caseNumber) + ': ' + win + ' won\n')
            answerFound = True
        else:
            countX = 0
            countO = 0
    #Draw
    if answerFound == False:
        dotsNumber = 0
        for element in case:
            if '.' in element:
                dotsNumber += 1
        if dotsNumber == 0:
            f.writelines('Case #' + str(caseNumber) + ': Draw\n')
        else:
            f.writelines('Case #' + str(caseNumber) + ': Game has not completed\n')
    answerFound = False