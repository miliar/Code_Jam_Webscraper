def allSame(a,b,c,d):
    areSame = False
    TLocation = -1

    array = [a,b,c,d]

    try:
        TLocation = array.index('T')
    except ValueError:
        TLocation = -1

    if TLocation != -1:
        array.pop(TLocation)
        if array[0] == array[1] and array[0] == array[2]:
            areSame = True
    elif TLocation == -1:
        if array[0] == array[1] and array[0] == array[2] and array[0] == array[3]:
            areSame = True


    return (areSame, array[0])


def segmentArrays(array):
    newArray = []
    while array != []:
        newArray.append(array[0:4])
        array.pop(0)
        array.pop(0)
        array.pop(0)
        array.pop(0)
        if array == []:
            break
        array.pop(0)
    return newArray

def checkForWin(array):
    win = False
    winner = None
    for i in xrange(0,4):
        result = allSame(array[i][0][0],array[i][0][1],array[i][0][2],array[i][0][3])
        if result[0] == True and result[1] != '.':
            winner = result[1]
            win = True
    for i in xrange(0,4):
        result = allSame(array[0][0][i],array[1][0][i],array[2][0][i],array[3][0][i])
        if result[0] == True and result[1] != '.':
            winner = result[1]
            win = True
    result = allSame(array[0][0][0],array[1][0][1],array[2][0][2],array[3][0][3])
    if result[0] == True and result[1] != '.':
        winner = result[1]
        win = True
    result = allSame(array[3][0][0],array[2][0][1],array[1][0][2],array[0][0][3])
    if result[0] == True and result[1] != '.':
        winner = result[1]
        win = True

    if win == True:
        return winner
    else:
        return 'N'




def checkForFinished(array):
    notFinished = True

    for i in xrange(0,4):
        for j in xrange(0,4):
            if array[i][0][j] == '.':
                notFinished = False

    return notFinished



def processResults(array):
    output = []
    for i in array:
        if i == 'X':
            output.append("X won")
        elif i == 'O':
            output.append("O won")
        elif i == True:
            output.append("Draw")
        elif i == False:
            output.append("Game has not completed")
    return output

def main(array):
    results = []
    for board in array:
        game = checkForWin(board)
        if game == 'N':
            game = checkForFinished(board)
        results.append(game)


    output = processResults(results)
    

    return output


x = 0
in_file = open('C:\Users\Zane\SkyDrive\CodeJam\input.in', 'r')
data = in_file.readlines()
new_data = []
for item in data[1:-1]: #Note that we are indexing after the first item to avoid the first line. We also skip the last item due to losing the last digit because the new line character isn't there.
    new_data.append(item[:-1].split())
new_data.append(data[-1].split()) #This is to add the last item on the end
in_file.close()
output_array = main(segmentArrays(new_data))



output = open('C:\Users\Zane\SkyDrive\CodeJam\output.out', 'w')
event = 1
for item in output_array:
    #x = main(int(item[0]),int(item[1]))
    output.write("Case #" + str(event) + ": " + str(item) + '\n')
    event += 1

output.close()
