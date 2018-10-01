def getArrangement():
    rows = 4
    matrix = [[] for i in range(4)]
    for i in range(rows):
        line = fi.readline().rstrip().split(' ')
        matrix[i] = line
    return matrix

def process(answerOne, answerTwo, arrangementOne, arrangementTwo):
    rowOne = arrangementOne[answerOne]
    rowTwo = arrangementTwo[answerTwo]
    rowlength = 4
    possible = []
    for i in range(rowlength):
        if rowOne[i] in rowTwo:
            possible.append(rowOne[i])
    if(len(possible)==0):
        fo.write("Volunteer cheated!")
    elif(len(possible) == 1):
        fo.write(str(possible[0]))
    else:
        fo.write("Bad magician!")
    fo.write("\n")

# algorithm

fi = open('A-small-attempt0.in')
fo = open('outputOne.out', 'w')

num_cases = (int)(fi.readline())

for i in range(num_cases):
    fo.write("Case #")
    fo.write(str(i+1) + ":" + " ")
    answerOne = (int)(fi.readline()) - 1
    arrangementOne = getArrangement()
    answerTwo = (int)(fi.readline()) - 1
    arrangementTwo = getArrangement()
    process(answerOne, answerTwo, arrangementOne, arrangementTwo)

fi.close()
fo.close()
