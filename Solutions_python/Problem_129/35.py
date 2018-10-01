#strat: give fresh tickets to exiting people

def calcCost(entry, ex, N):
    diff = ex-entry
    return diff*N - (diff-1)*diff/2

def normalCost(N, passengers):
    cost = 0
    for p in passengers:
        cost += p[2] * calcCost(p[0],p[1],N)
    return cost

def swappingCost(N, passengers):
    passengers.sort()
    ticketEntries = []
    exiters = {}
    cost = 0

    enterexits = []
    for p in passengers:
        if p[0] not in enterexits:
            enterexits += [p[0]]
        if p[1] not in enterexits:
            enterexits += [p[1]]
    enterexits.sort()
    
    for i in enterexits:
        #print i, ticketEntries, exiters
        # Add passengers coming in at this station
        if passengers != []:
            p = passengers[0]
            while(p[0] == i):
                ticketEntries += [[i, p[2]]]
                if p[1] in exiters:
                    exiters[p[1]] += p[2]
                else:
                    exiters[p[1]] = p[2]
                
                passengers.pop(0)
                if passengers == []:
                    break
                p = passengers[0]

        # Give leavers the freshest tickets
        ticketEntries.sort()
        if i not in exiters:
            continue
        else:
            numExiters = exiters[i]
            #print numExiters, ticketEntries
            while numExiters > 0 and numExiters >= ticketEntries[-1][1]:
                #print numExiters, ticketEntries
                cost += calcCost(ticketEntries[-1][0], i, N) * ticketEntries[-1][1]
                numExiters -= ticketEntries[-1][1]
                ticketEntries.pop(-1)
                #print numExiters, ticketEntries
            if numExiters != 0:
                cost += calcCost(ticketEntries[-1][0], i, N) * numExiters
                ticketEntries[-1][1] = ticketEntries[-1][1] - numExiters
            #print numExiters, ticketEntries
    return cost


filename = "A-large (4).in"
outputname = filename + 'out.txt'

inFile = open(filename, 'r')
outFile = open(outputname, 'w')

numTests = int(inFile.readline())

for i in range(numTests):
    test = inFile.readline().split()
    N = int(test[0])
    P = int(test[1])
    passengers = []
    for j in range(P):
        c = inFile.readline().split()
        passengers += [(int(c[0]), int(c[1]), int(c[2]))]
    orig = normalCost(N, passengers)
    #print orig
    new = swappingCost(N, passengers)
    #print new
    diff = (orig-new) % 1000002013
    outFile.write("Case #" + str(i+1) + ": " + str(diff) + '\n')
    print "Case #" + str(i+1) + ": " + str(diff) + '\n'
    
inFile.close()
outFile.close() 
            
