
# given array of form [('0' 1) ('B' 2)...]
def lenCritPath(commands):
    curOrgCmd = 0
    curBlueCmd = 0
    curOrgPos = 1
    curBluePos = 1
    time = 0
    ttlCmds = len(commands)

    while True:

        #advance the pointers forward until they are on their own commands
        while curOrgCmd < ttlCmds and commands[curOrgCmd][0] != 'O':
            curOrgCmd += 1
            
        while curBlueCmd < ttlCmds and commands[curBlueCmd][0] != 'B':
            curBlueCmd += 1

        if curOrgCmd == ttlCmds and curBlueCmd == ttlCmds:
            break;

        time += 1
        #each takes one step towards their own goal
        pressed = False
        if curOrgCmd < ttlCmds:
            orgDest = commands[curOrgCmd][1]
            if orgDest > curOrgPos:
                curOrgPos += 1
            elif orgDest < curOrgPos:
                curOrgPos -= 1
            elif curOrgCmd < curBlueCmd:
                #standing on it, press button and advance command
                curOrgCmd += 1
                pressed = True

        if curBlueCmd < ttlCmds:
            blueDest = commands[curBlueCmd][1]
            if blueDest > curBluePos:
                curBluePos += 1
            elif blueDest < curBluePos:
                curBluePos -= 1
            elif curBlueCmd < curOrgCmd:
                # standing on it 
                curBlueCmd += 1

    return time


fin = open("large.in", "r")
fout = open("large.out", "w")

line = fin.readline()

numCases = int(line)
curCase = 1
while curCase <= numCases:
    line = fin.readline()
    elements = line.split()
    numElements = int(elements[0])
    commands = []
    for i in range(1, 1+2*numElements, 2):
        commands.append( (elements[i], int(elements[i+1])) )
    time = lenCritPath(commands)
    fout.write("Case #" + str(curCase) + ": " + str(time) + "\n");
    curCase += 1

fin.close()
fout.close()
        
