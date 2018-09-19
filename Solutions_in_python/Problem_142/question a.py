def foo(strings):
    #process into list of repeated chars
    stringsGrouping = []
    for i in range(len(strings)):
        charGrouping = []
        previousChar = ""
        #print("Before: " + strings[i])
        for j in range(len(strings[i])):
            if strings[i][j] == previousChar:
                charGrouping[-1] += strings[i][j]
            else:
                charGrouping.append(strings[i][j])
            previousChar = strings[i][j]
        if "\n" in charGrouping: 
            charGrouping.remove("\n")
        #print("After: " + str(charGrouping))
        stringsGrouping.append(charGrouping)


    #format: stringsGroupings[string][repeatedChar]
    #find mean length for all elements of stringsGrouping
    averageLengths = []
    changes = 0
    for i in range(len(stringsGrouping[0])):
        averageLengths.append(0)
        for j in range(len(stringsGrouping)):
            if len(stringsGrouping[0]) != len(stringsGrouping[j]):
                return "Fegla Won"
            if stringsGrouping[0][i][0] != stringsGrouping[j][i][0]:
                return "Fegla Won"
            averageLengths[i] += len(stringsGrouping[j][i])
        averageLengths[i] = averageLengths[i]/len(stringsGrouping)
        averageLengths[i] = int(round(averageLengths[i], 0))
        for j in range(len(stringsGrouping)):
            changes += abs(averageLengths[i] - len(stringsGrouping[j][i]))
    return changes


file = open("A-small-attempt0.in.txt", "r")
output = open("A-small-attempt0.out.txt", "w")
T = int(file.readline())
for i in range(T):
    strings = []
    N = int(file.readline())
    for j in range(N):
        strings.append(str(file.readline()))
    output.write("Case #" + str(i+1) + ": " + str(foo(strings)) + "\n")

file.close()
output.close()

