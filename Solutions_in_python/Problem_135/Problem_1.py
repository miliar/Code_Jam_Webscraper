inputs = open("inputs.txt", 'r')
outputs = open("outputs.txt", 'w')
nCases = int(inputs.readline())
for currentCase in range(nCases):
    firstRow = int(inputs.readline())
    for i in range(firstRow):
        firstPossible = inputs.readline()
    for i in range(4-firstRow):
        inputs.readline()

    secondRow = int(inputs.readline())
    for i in range(secondRow):
        secondPossible = inputs.readline()
    for i in range(4-secondRow):
        inputs.readline()


    firstPossible = firstPossible.split()
    secondPossible = secondPossible.split()
    
    setRows = []
    for posGuess in firstPossible:
        if posGuess in secondPossible:
            setRows.append(posGuess)
    for posGuess in secondPossible:
        if posGuess in firstPossible and posGuess not in setRows:
            setRows.append(posGuess)

    print posGuess
    if(len(setRows) == 1): #successCase #1: 7
        outputs.write("Case #" + str(currentCase+1) + ": " + str(setRows[0]))
    elif(len(setRows) == 0):
        outputs.write("Case #" + str(currentCase+1) + ": " + "Volunteer cheated!")
    else:
        outputs.write("Case #" + str(currentCase+1) + ": " + "Bad magician!")
    outputs.write("\n")
    
inputs.close()
outputs.close()
    
    
    
