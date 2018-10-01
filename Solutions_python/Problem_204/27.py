from __future__ import print_function
import sys

# print to stderr for debugging
enableDebug = False
def printe(*stuff):
    if enableDebug:
        print(*stuff, file=sys.stderr) 


# Open file for processing
filename = sys.argv[1]
inputFile = open(filename, 'r')
lines = [l.rstrip('\n') for l in inputFile]
linesIter = iter(lines)
nCases = int(linesIter.next())


# Process each case
for iCase in range(1,nCases+1):
    printe("\nProcessing case " + str(iCase))

    # Solve problem
    items = linesIter.next().split()
    nIngredients = int(items[0])
    nPackets = int(items[1])

    ingredientsNeeded = [int(x) for x in linesIter.next().split()]

    packets = []
    for iI in range(nIngredients):

        thisPackets = [int(x) for x in linesIter.next().split()]
        thisPackets.sort()
        packets.append(thisPackets)


    nPackets = 0
    packetSize = 1
    while True:

        printe("\n\nTrying size " + str(packetSize))

        anyChanged = False
        canMake = True
        minCanMake = 1E15
        for iI in range(nIngredients):

            printe("Processing ingrdient " + str(iI))
                
            if(len(packets[iI]) == 0): 
                printe("Skipping empty ingredient")
                canMake = False
                continue

            lowerLim = packetSize * ingredientsNeeded[iI] * 9
            upperLim = packetSize * ingredientsNeeded[iI] * 11
            nAvail = 10*packets[iI][0]
            

            # Discard if strictly too small
            if nAvail < lowerLim:
                printe("Discarding small ingredient")
                packets[iI] = packets[iI][1:]
                anyChanged = True
                canMake = False

            # If strictly too large, note next size
            elif nAvail > upperLim:
                printe("Recording large ingredient")
                minCanMake = min((minCanMake, (packets[iI][0] * 10) / (11 * ingredientsNeeded[iI]) - 1))
                canMake = False


        # Make a kit
        if canMake:
            printe("== Making kit!")
            nPackets += 1
            for iI in range(nIngredients):
                packets[iI] = packets[iI][1:]
            anyChanged = True

        if not anyChanged:
            packetSize = max((minCanMake, packetSize+1))
                
        if not anyChanged and minCanMake == 1E15:
            break


    print("Case #{}: {}".format(iCase, nPackets))
