t = int(raw_input())

for n in range(t):
    line = [None for i in range(4)]
    column = ['' for i in range(4)]
    winner = None
    incomplete = False
    for j in range(4):
        line[j] = raw_input()
        column[0] += line[j][0]
        column[1] += line[j][1]
        column[2] += line[j][2]
        column[3] += line[j][3]

    raw_input() #ignore empty line

    #check lines and columns
    for j in range(4):
        linelist = list(line[j])
        linelist = sorted(linelist)
        linesorted = ''.join(linelist)
        columnlist = list(column[j])
        columnlist = sorted(columnlist)
        columnsorted = ''.join(columnlist)
        if linesorted == 'TXXX' or linesorted == 'XXXX' or columnsorted == 'TXXX' or columnsorted == 'XXXX':
            winner = 'X'
        elif linesorted == 'OOOT' or linesorted == 'OOOO' or columnsorted == 'OOOT' or columnsorted == 'OOOO':
            winner = 'O'
        elif '.' in linesorted:
            incomplete = True

    diaglist = sorted([line[i][i] for i in range(4)])
    diagsorted = ''.join(diaglist)
    if diagsorted == 'TXXX' or diagsorted == 'XXXX':
        winner = 'X'
    elif diagsorted == 'OOOT' or diagsorted == 'OOOO':
        winner = 'O'

    diaglist = sorted([line[3-i][i] for i in range(4)])
    diagsorted = ''.join(diaglist)
    if diagsorted == 'TXXX' or diagsorted == 'XXXX':
        winner = 'X'
    elif diagsorted == 'OOOT' or diagsorted == 'OOOO':
        winner = 'O'

    result = ""
    if winner == 'X':
        result = 'X won'
    elif winner == 'O':
        result = 'O won'
    elif incomplete:
        result = 'Game has not completed'
    else:
        result = 'Draw'

    print "Case #" + str(n+1) + ": " + result


