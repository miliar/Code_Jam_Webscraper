import sys

if len(sys.argv) == 1:
    print("No input file provided.")
    sys.exit()
else:
    filename = sys.argv[1]
    try:
        fileobject = open(filename, 'r')
    except:
        print("Failed to open given file.")
        sys.exit()
    try:
        firstLine = fileobject.readline()
    except:
        print("Failed to read first line.")
        sys.exit()
    datasetSize = int(firstLine)
    if not datasetSize:
        print("Unable to parse dataset size.")
        sys.exit()
    lineNr = 1
    for i in range(datasetSize):
        lineNr = lineNr + 1
        try:
            lineText = fileobject.readline()
        except:
            print("Failed to read line ", lineNr)
            sys.exit()
        if lineText[-1] == "\n":
            textToParse = lineText[0:-1]
        else:
            textToParse = lineText
        inputParams = textToParse.split(" ")
        Smax = int(inputParams[0]) # size of omino
        Slist = list(map(int, inputParams[1])) # list of shyness levels and people present
        peopleClapping = Slist[0]
        toInvite = 0
        for shyness in range(1, len(Slist)):
            if peopleClapping < shyness:
                newToInvite = shyness - peopleClapping
                toInvite += newToInvite
                peopleClapping = shyness
            peopleClapping += Slist[shyness]
        if i == 0:
            startCharacter = ""
        else:
            startCharacter = "\n"
        print(startCharacter, "Case #", i+1, ": ", toInvite, end="", sep="")