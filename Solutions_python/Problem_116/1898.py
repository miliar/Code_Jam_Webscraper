
def checkGame(TwoDArray):
    
    state = checkVerts(TwoDArray)
    if state == 0:
        state = checkHor(TwoDArray)
    if state == 0:
        state = checkDiag1(TwoDArray)
    if state == 0:
        state = checkDiag2(TwoDArray)
    if state > 0:
        if state == 1:
            print "X wins"
        elif state == 2:
            print "O wins"
        return state
    else:
        if checkCompleted(TwoDArray) == 0:
            print "Not Complete"
            return -1
        else:
            print "Draw"
            return 0
        

def checkCompleted(TwoDArray):
    for i in range(0,4):
        for j in range(0,4):
            if TwoDArray[i][j] == ".":
                return 0
    return 1

def checkVerts(TwoDArray):
    array = []
    for i in range(0,4):
        array.append(TwoDArray[0][i])
        array.append(TwoDArray[1][i])
        array.append(TwoDArray[2][i])
        array.append(TwoDArray[3][i])
        result = findCase(array)
        #print array
        array = []
        if result > 0:
            #print "Verts: " + str(result)
            return result 
    return 0

def checkHor(TwoDArray):
    array = []
    for i in range(0,4):
        array.append(TwoDArray[i][0])
        array.append(TwoDArray[i][1])
        array.append(TwoDArray[i][2])
        array.append(TwoDArray[i][3])
        result = findCase(array)
        #print array
        array = []
        if result > 0:
            #print "Hors " + str(result)
            return result 
    return 0

def checkDiag1(TwoDArray):
    array = []
    for i in range(0,4):
        array.append(TwoDArray[i][i])
    result = findCase(array)
    #print "Diag1 " + str(result)
    return result

def checkDiag2(TwoDArray):
    array = []
    for i in range(3,-1,-1):
        array.append(TwoDArray[3-i][i])
    result = findCase(array)
    #print "Diag2 " + str(result)
    return result

def findCase(array):
    dic = {}
    for char in array:
        if char in dic:
            dic[char] += 1
        else:
            dic[char] = 1
    #print dic
    if 'X' in dic and 'T' in dic:
        #print "X found and T found"
        if dic['X'] > 2 and dic['T'] == 1:
            return 1
    elif 'X' in dic:
        #print "X found"
        if dic['X'] > 3: return 1

    elif 'O' in dic and 'T' in dic:
        #print "O and T found"
        if dic['O'] > 2 and dic['T'] == 1:
            return 2
    elif 'O' in dic:
        #print "O found"
        if dic['O'] > 3: return 2
    
    return 0

f = open('p1_large.in','r')

w = open('problem1_output.txt','w')
counter = 0
array = []
for line in f:
    if counter == 0:
        numTests = int(line)
        counter += 1
    else:
        if line != "\n":
            array.append(line.strip())
        else:
            array = []
        if len(array) == 4:
            if checkGame(array) == 0:
                w.write("Case #"+str(counter)+ ": Draw" + "\n")
            elif checkGame(array) == -1:
                w.write("Case #"+str(counter)+ ": Game has not completed" + "\n")
            elif checkGame(array) == 1:
                w.write("Case #"+str(counter)+ ": X won" + "\n")
            elif checkGame(array) == 2:
                w.write("Case #"+str(counter)+ ": O won" + "\n")   
            counter += 1
            #print "New Test"

if counter-1 != numTests: print "Not enough results"

print numTests

w.close()
f.close()
