import sys

def botTrust(line):
    seq = line.split()
    numMoves = int(seq[0])
    moves = seq[1:]
    lastColor = None
    lastBlue  = 1
    lastOrng  = 1
    blueWait  = 0
    orngWait  = 0
    totalSum  = 0
    for i in range(0, len(moves), 2):
        color, button = moves[i], int(moves[i+1])
        if (color == 'B'):
            travelTime = abs(button - lastBlue) + 1
            if(lastColor == 'B'):
                orngWait += travelTime
            else:
                travelTime = max(travelTime - blueWait, 1)
                orngWait  = travelTime
            lastBlue  = button
            lastColor = 'B'
            totalSum += travelTime
        else:
            travelTime = abs(button - lastOrng) + 1
            if(lastColor == 'O'):
                blueWait += travelTime
            else:
                travelTime = max(travelTime - orngWait, 1)
                blueWait  = travelTime
            lastOrng  = button
            lastColor = 'O' 
            totalSum += travelTime
    return totalSum

filename = sys.argv[1]
f = open(filename, 'r')
testCases = int(f.readline().split()[0])
for i in range(testCases):
    totaltime = botTrust(f.readline())
    print("Case #" + str(i + 1) + ": " + str(totaltime))
f.close()
