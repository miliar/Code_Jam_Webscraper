import sys

inputFile = sys.argv[1]
outputFile = sys.argv[2]

input = open(inputFile, 'r')
content = input.read()
input.close()

content = content.splitlines()
numCases = int(content[0].split()[0])
content = content[1:]

output = open(outputFile, "w")

for i in range(numCases):
    counter = 0
    numbers = content[i].split()
    A = int(numbers[0])
    B = int(numbers[1])
    k = A
    length = len(numbers[0])
    while k < B:
        # initialize numStr
        numStr = str(k)
        numList = [] # keep track of all arrangements
        # find all arrangeement of the sequence
        for m in range(length-1): 
            # shift the sequence by 1
            temp = numStr
            numStr = ""
            for n in range(length):
                numStr = numStr + temp[n-1]

            if numStr in numList: # avoid repeating the same rearrangement
                continue

            numList.append(numStr) # to keep track of what has already been seen

            num = int(numStr)
            if num > k and num <= B:
                counter = counter + 1
        k = k + 1
    output.write("Case #" + str(i+1) + ": " + str(counter) + "\n")

output.close()

