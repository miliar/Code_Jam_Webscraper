#!/usr/bin/env python
print("Enter file name: ")
inFileName = input()
print("Enter output name: ")
outFileName = input() + ".txt"

inFile = open(inFileName, 'r')

data = inFile.readlines()

data = [line.strip("\n") for line in data]

def solveProblem(n):
    maxi = n
    while(True):
        valid = True
        prevDigit = int(maxi[0])
        for i in range(len(maxi)):
            if int(maxi[i]) < prevDigit:
                valid = False
                maxi = maxi[:(i-1)] + str(int(maxi[i-1])-1) + '9'*len(maxi[i:])
                break
            prevDigit = int(maxi[i])
        if valid:
            return maxi

def removeZeros(string):
    while string[0] == '0':
        string = string[1:]
    return string

nInputs = data[0]
data.pop(0)

results = []

print(data)

for line in data:
    results += [removeZeros(solveProblem(line))]


outFile = open(outFileName,"w") 

for i in range(int(nInputs)):
    line = "Case #{}: {}\n".format(i + 1, results[i])
    outFile.write(line)
    print(line.strip("\n"))
 
outFile.close()


