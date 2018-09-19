import math
#YOLOSWAG
def getRepeats(string):
    last = ""
    repeats = []
    cur = -1
    for c in string:
        if c == last:
            repeats[cur][1] += 1
        else:
            repeats.append([c,1])
            cur += 1
        last = c
    return repeats
def getMoves(checkLengths, repeats):
    moves = 0
    for x in range(0,checkLengths):
        bestMove = -1
        for a in repeats:
            checkMoves = 0
            charCompare = a[x][0]
            for b in repeats:
                if b[x][0] == charCompare:
                    checkMoves += abs(a[x][1] - b[x][1])
                else:
                    return -1
            if bestMove == -1 or bestMove > checkMoves:
                bestMove = checkMoves
        moves += bestMove
    return moves
                    
inputs = open("in.txt").readlines()
output = open('out.txt', 'w')
t = int(inputs[0])
r = 1
for i in range(1, t + 1):
    #r = (i - 1) * 3 + 1
    n = int(inputs[r])
    r += 1
    repeats = []
    for j in range(0, n):
        repeats.append(getRepeats(inputs[r].rstrip()))
        r+=1
    moves = 0
    checkLengths = -1
    for re in repeats:
        if checkLengths == -1:
            checkLengths = len(re)
        if len(re) != checkLengths:
            checkLengths = -1
            break
    if checkLengths == -1:
        answer = "Case #%d: Fegla Won\n"%(i)
    else:   
        moves = getMoves(checkLengths, repeats)
        if(moves == -1):
            answer = "Case #%d: Fegla Won\n"%(i)
        else:
            answer = "Case #%d: %d\n"%(i,moves) 
    print(answer)
    output.write(answer)
output.close()
