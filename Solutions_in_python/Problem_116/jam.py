
#inputFile = 'input.txt'
inputFile = 'A-large.in'
outputFile = 'output.txt'

f = open(inputFile, 'rb')
inputs = f.readlines()
f.close()

total = int(inputs[0])
count = 1

def isWiner(line, player):
    if line.count(player) + line.count('T') == 4:
        return True
    else:
        return False

def test(moves, count):
    notComplete = False
    for j in range(4):
        row = moves[j]
        column = moves[0][j]+moves[1][j]+moves[2][j]+moves[3][j]
        if isWiner(row, 'O') or isWiner(column, 'O'):
            return 'Case #%d: O won' %count
        if isWiner(row, 'X') or isWiner(column, 'X'):
            return 'Case #%d: X won' %count
        if '.' in row:
            notComplete = True
    rc = moves[0][0]+moves[1][1]+moves[2][2]+moves[3][3]
    cr = moves[0][3]+moves[1][2]+moves[2][1]+moves[3][0]

    if isWiner(rc, 'O') or isWiner(cr, 'O'):
        return 'Case #%d: O won' %count
    if isWiner(rc, 'X') or isWiner(cr, 'X'):
        return 'Case #%d: X won' %count
    if notComplete:
        return 'Case #%d: Game has not completed' %count
    else:
        return 'Case #%d: Draw' %count
        
i = 1
result = ''
while i < len(inputs):
    moves =['','','','']
    moves[0]=inputs[i].replace('\r','').replace('\n','')
    moves[1]=inputs[i+1].replace('\r','').replace('\n','')
    moves[2]=inputs[i+2].replace('\r','').replace('\n','')
    moves[3]=inputs[i+3].replace('\r','').replace('\n','')
    i+=5
    result += test(moves, count) + '\r\n'
    count += 1

f=open(outputFile,'wb')
f.write(result)
f.close()
    
