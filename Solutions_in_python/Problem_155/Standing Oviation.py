# Standing oviation
try:
    # Write file
    output = open('StandingOviationOutput.txt', 'w')
    # Read file
    file = open('A-large.in', 'r')
    file = file.readlines()
    testcases = int(file[0].rstrip())
    for i in range(1, testcases+1):
        line = file[i].split()
        SMax = int(line[0])
        SMaxString = line[1]
        if SMaxString[-1] == 0:
            print("There must be at least one person in the audience!")
        elif SMax+1 != len(SMaxString):
            print("SMax+1 must be equal to length of string!")
        else: # carry on
            j = 0
            noOviation = 0
            noNeeded = 0
            print("case:" , i)
            while j != (len(SMaxString)):
                if SMaxString[j] == 0:
                    j += 1
                elif noOviation + noNeeded >= j:
                    noOviation = noOviation + int(SMaxString[j])
                    j += 1
                else:   # if noOviation < j
                    noNeeded = noNeeded + (j - (noOviation + noNeeded))
                    noOviation = noOviation + int(SMaxString[j])
                    j += 1
            output.write("Case #%d: %d\n" % (i, noNeeded))
                
    output.close()
    
except FileNotFoundError:
    print('File Not Found!')

