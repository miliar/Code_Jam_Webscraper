__author__ = 'Michael'


def handleCase(caseNo, case):
    X_WON = 1
    O_WON = 2
    result = 0
    emptyPresent = False

    d1X = 0; d1O = 0
    d2X = 0; d2O = 0
    for i in xrange(4):
        cX = 0; rX = 0
        cO = 0; rO = 0
        for j in xrange(4):
            #Check row
            if case[i][j] == 'X': rX += 1
            elif case[i][j] == 'O': rO += 1
            elif case[i][j] == 'T': rX += 1; rO += 1
            else: emptyPresent = True
            #Check column
            if case[j][i] == 'X': cX += 1
            elif case[j][i] == 'O': cO += 1
            elif case[j][i] == 'T': cX += 1; cO += 1
            else: emptyPresent = True

        if cX == 4 or rX == 4:
            result = X_WON
            break
        elif cO == 4 or rO == 4:
            result = O_WON
            break

        if case[i][i] == 'X': d1X += 1
        elif case[i][i] == 'O': d1O += 1
        elif case[i][i] == 'T': d1X += 1; d1O += 1;

        if case[3-i][i] == 'X': d2X += 1
        elif case[3-i][i] == 'O': d2O += 1
        elif case[3-i][i] == 'T': d2X += 1; d2O += 1;

    if result == 0:
        if d1X == 4 or d2X == 4:
            result = X_WON
        elif d1O == 4 or d2O == 4:
            result = O_WON

    if  result == 0:
        if emptyPresent:
            #In progress
            message = 'Game has not completed'
        else:
            #Draw
            message = 'Draw'
    elif result == X_WON:
        #X won
        message = 'X won'
    else:
        #O won
        message = 'O won'

    print 'Case #%d: %s' % (caseNo, message)

numCases = int(raw_input().strip())

for caseNo in xrange(numCases):
    #Handle Case
    case = list()
    for i in xrange(4):
        case.append(raw_input().strip())
    try:
        raw_input()
    except Exception:
        pass
    handleCase(caseNo+1, case)