f = open('A-large.in.txt', 'rU')

numberOfCases = int(f.readline())
outputString = ""
i = 0

while i < numberOfCases:
    gridList = []
    gridList.append(f.readline().rstrip())
    gridList.append(f.readline().rstrip())
    gridList.append(f.readline().rstrip())
    gridList.append(f.readline().rstrip())
    blank = f.readline()

    win = False

    # Horizontal
    for line in gridList:
        if (line.count('X') == 3 and line.count('T') == 1) or (line.count('X') == 4):
            print "Case #" + str(i+1) + ": X won"
            outputString += "Case #" + str(i+1) + ": X won\n"
            win = True
            break
        elif (line.count('O') == 3 and line.count('T') == 1) or (line.count('O') == 4):
            print "Case #" + str(i+1) + ": O won"
            outputString += "Case #" + str(i+1) + ": O won\n"
            win = True
            break

    # Vertical
    if win == False:

        for columnIndex in xrange(0, 4):
            column = ""
            for line in gridList:
                column += line[columnIndex]
            if (column.count('X') == 3 and column.count('T') == 1) or (column.count('X') == 4):
                print "Case #" + str(i+1) + ": X won"
                outputString += "Case #" + str(i+1) + ": X won\n"
                win = True
                break
            elif (column.count('O') == 3 and column.count('T') == 1) or (column.count('O') == 4):
                print "Case #" + str(i+1) + ": O won"
                outputString += "Case #" + str(i+1) + ": O won\n"
                win = True
                break

    if win == False:

        # Diagonal (down)
        diagonalIndex = 0
        diagonalDown = ""
        for line in gridList:
            diagonalDown += line[diagonalIndex]
            diagonalIndex = diagonalIndex + 1

        if (diagonalDown.count('X') == 3 and diagonalDown.count('T') == 1) or (diagonalDown.count('X') == 4):
            print "Case #" + str(i + 1) + ": X won"
            outputString += "Case #" + str(i + 1) + ": X won\n"
            win = True
        elif (diagonalDown.count('O') == 3 and diagonalDown.count('T') == 1) or (diagonalDown.count('O') == 4):
            print "Case #" + str(i+1) + ": O won"
            outputString += "Case #" + str(i+1) + ": O won\n"
            win = True

    if win == False:

        # Diagonal (up)
        diagonalIndex = 3
        diagonalUp = ""
        for line in gridList:
            diagonalUp += line[diagonalIndex]
            diagonalIndex = diagonalIndex - 1

        if (diagonalUp.count('X') == 3 and diagonalUp.count('T') == 1) or (diagonalUp.count('X') == 4):
            print "Case #" + str(i + 1) + ": X won"
            outputString += "Case #" + str(i + 1) + ": X won\n"
            win = True
        elif (diagonalUp.count('O') == 3 and diagonalUp.count('T') == 1) or (diagonalUp.count('O') == 4):
            print "Case #" + str(i + 1) + ": O won"
            outputString += "Case #" + str(i + 1) + ": O won\n"
            win = True

    if win == False:

        # Check for draw
        for line in gridList:
            draw = True
            if line.count('.') > 0:
                draw = False
                break

        if (draw == True):
            print "Case #" + str(i + 1) + ": Draw"
            outputString += "Case #" + str(i + 1) + ": Draw\n"
        else:
            print "Case #" + str(i + 1) + ": Game has not completed"
            outputString += "Case #" + str(i + 1) + ": Game has not completed\n"

    # Increment counter
    i = i + 1

f.close();

fo = open("output.txt","w")
fo.write(outputString[:-1])
fo.close()