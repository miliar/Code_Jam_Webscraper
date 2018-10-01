def solve(q):
    q = q.split(" ")
    q = q[1:]
    
    pos = dict()
    pos["O"], pos["B"] = 1, 1

    ltime = dict()
    ltime["O"], ltime["B"] = 0, 0

    time = 0
    
    for i in range((len(q)+1)/2):
        (robot, position) = (q[2*i], q[2*i+1])
        
        position = int(position)
        ltime[robot] += abs(pos[robot] - position) + 1
        pos[robot] = position
        if time < ltime[robot]:
            time = ltime[robot]
        else:
            time = time + 1
            ltime[robot] = time

    return time

fIn     = open('aInput', 'r')
fOut    = open('aOutput', 'r+')

i = 0
for line in fIn:
    i += 1
    print line
    fOut.write("Case #" + str(i) + ": " + str(solve(line[:-1])) + "\n")
