import sys
import re

inputArray = []
countFlag = False
Report = []

inputFile = sys.argv[1]
outputFile = sys.argv[2]

print "inputFile: " + inputFile
print "outputFile: " + outputFile

# Read in input file
fp = open(inputFile, 'r')
try:
    for line in fp:
        if (countFlag == False):
            countFlag = True
            T = int(line)
            continue

        line = line.strip()
        inputArray.append(line)

finally:
    fp.close()


#Loop through 'T' test cases
T_count = 0
while T_count < T:
    finished = False
    intBeingTested = int(inputArray[T_count])

    #Stay in while loop until whole integer is checked and flag is set
    while finished == False:
        intTestArray = map(int, str(intBeingTested))

        #if it is a single number, no need to check
        if len(intTestArray) == 1:
            finished = True
            continue

        # Loop through all numbers in integet
        i = len(intTestArray) - 1
        while i >= 1:
            tempInt = 0
            if int(intTestArray[i]) < int(intTestArray[i - 1]):
                tempArray = [0 for j in range(len(intTestArray) - i)]
                j = 0
                while ((j + i) < (len(intTestArray)) ):
                    tempArray[j] = intTestArray[i+j]
                    j = j + 1
                tempInt = int(''.join(map(str, tempArray))) + 1
                intBeingTested = int(''.join(map(str, intTestArray)))
                intBeingTested = intBeingTested - tempInt
                intTestArray = map(int, str(intBeingTested))
            else:
                i = i - 1

        if i <= 0:
            finished = True

    # Add to report list
    reportString = "Case #" + str(int(T_count+1)) + ": " + str(intBeingTested) + "\n"
    Report.append(reportString)

    T_count = T_count + 1

#Write output file
fp = open(outputFile, 'w')
try:
    for line in Report:
        fp.write(line)

finally:
    fp.close()
