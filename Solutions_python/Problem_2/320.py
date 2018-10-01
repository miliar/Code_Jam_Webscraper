inFile = open("B-large.in", "r")
outFile = open("B-large-out.out", "w")

cases = int(inFile.readline())

for caseNum in range(cases):
    # get and massage data input
    StationArrivalsA = []
    StationDeparturesA = []

    StationArrivalsB = []
    StationDeparturesB = []

    turnaround = int(inFile.readline())

    splitLine = inFile.readline().split(" ")
    NA = int(splitLine[0])
    NB = int(splitLine[1])

##    print NA, NB

    for i in range(NA):
        splitLine = inFile.readline().split(" ")
        departureString = splitLine[0]
        arrivalString = splitLine[1]

        departureSplit = departureString.split(":")
        hours = int(departureSplit[0])
        minutes = int(departureSplit[1])
        StationDeparturesA.append(60 * hours + minutes)

        arrivalSplit = arrivalString.split(":")
        hours = int(arrivalSplit[0])
        minutes = int(arrivalSplit[1])
        StationArrivalsB.append(60 * hours + minutes + turnaround)

    for i in range(NB):
        splitLine = inFile.readline().split(" ")
        departureString = splitLine[0]
        arrivalString = splitLine[1]

        departureSplit = departureString.split(":")
        hours = int(departureSplit[0])
        minutes = int(departureSplit[1])
        StationDeparturesB.append(60 * hours + minutes)

        arrivalSplit = arrivalString.split(":")
        hours = int(arrivalSplit[0])
        minutes = int(arrivalSplit[1])
        StationArrivalsA.append(60 * hours + minutes + turnaround)

    StationArrivalsA.sort()
    StationDeparturesA.sort()
    StationArrivalsB.sort()
    StationDeparturesB.sort()
    
##    print StationArrivalsA
##    print StationDeparturesA
##
##    print StationArrivalsB
##    print StationDeparturesB
##    print
##    print

    # Set up initial parameters

    trainsStartA = 0
    trainsStartB = 0

    trainsReadyA = 0
    trainsReadyB = 0

    # work with station A
    for t in range(1440):

        arrivalsClear = False
        while arrivalsClear == False:
            if len(StationArrivalsA) != 0 and StationArrivalsA[0] == t:
                trainsReadyA = trainsReadyA + 1
                StationArrivalsA.pop(0)
            else:
                arrivalsClear = True

        departuresClear = False
        while departuresClear == False:
            if len(StationDeparturesA) != 0 and StationDeparturesA[0] == t:
                if trainsReadyA > 0:
                    trainsReadyA = trainsReadyA - 1
                else:
                    trainsStartA = trainsStartA + 1
                StationDeparturesA.pop(0)
            else:
                departuresClear = True

    # work with station B
    for t in range(1440):

        arrivalsClear = False
        while arrivalsClear == False:
            if len(StationArrivalsB) != 0 and StationArrivalsB[0] == t:
                trainsReadyB = trainsReadyB + 1
                StationArrivalsB.pop(0)
            else:
                arrivalsClear = True

        departuresClear = False
        while departuresClear == False:
            if len(StationDeparturesB) != 0 and StationDeparturesB[0] == t:
                if trainsReadyB > 0:
                    trainsReadyB = trainsReadyB - 1
                else:
                    trainsStartB = trainsStartB + 1
                StationDeparturesB.pop(0)
            else:
                departuresClear = True

##    print trainsStartA, trainsStartB

    outputString = "Case #" + str(caseNum + 1) + ": " + str(trainsStartA) + " " + str(trainsStartB) + "\n"
    print outputString.rstrip()
    outFile.write(outputString)
        

inFile.close()
outFile.close()
