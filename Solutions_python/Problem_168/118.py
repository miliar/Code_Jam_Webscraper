import sys

iFile = open(sys.argv[1],"r")

T = int(iFile.readline().strip())

for t in range(T):
    line = iFile.readline().strip().split()
    rows = int(line[0])
    columns = int(line[1])
   
    impossible = False
    numChanges = 0

    field = []
    changeField = [[0]*columns for row in range(rows)] 

    for row in range(rows):
        field.append([])
        line = iFile.readline().strip()
        for column in range(columns):
            field[row].append(line[column])

    #up
    for column in range(columns):
        i = 0
        while True:
            if(field[i][column] != '.'):
                if(field[i][column] == '^'):
                    numChanges += 1
                changeField[i][column] += 1
                if(changeField[i][column] == 4):
                    impossible = True
                break
            else:
                i += 1
                if(i >= rows):
                    break
    #down
    for column in range(columns):
        i = rows - 1
        while True:
            if(field[i][column] != '.'):
                if(field[i][column] == 'v'):
                    numChanges += 1
                changeField[i][column] += 1
                if(changeField[i][column] == 4):
                    impossible = True
                break
            else:
                i -= 1
                if(i < 0):
                    break

    #left
    for row in range(rows):
        i = 0
        while True:
            if(field[row][i] != '.'):
                if(field[row][i] == '<'):
                    numChanges += 1
                changeField[row][i] += 1
                if(changeField[row][i] == 4):
                    impossible = True
                break
            else:
                i += 1
                if(i >= columns):
                    break

    #right
    for row in range(rows):
        i = columns - 1
        while True:
            if(field[row][i] != '.'):
                if(field[row][i] == '>'):
                    numChanges += 1
                changeField[row][i] += 1
                if(changeField[row][i] == 4):
                    impossible = True
                break
            else:
                i -= 1
                if(i < 0):
                    break

    if impossible:
        output = "IMPOSSIBLE"
    else:
        output = str(numChanges)
   
    print("Case #"+str(t+1)+": "+output)
