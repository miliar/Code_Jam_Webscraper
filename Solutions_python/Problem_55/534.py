import re

fileName = "input.txt"
fileName = "C-small-attempt0.in"
input = open(fileName)
outputFile = open("output-rollerCoaster-small.txt", "w")

def readLine(stream=input):
    return stream.readline().replace("\r","").replace("\n","")
    
def writeLine(text):
    outputFile.write(str(text).lstrip().rstrip() + "\n")
    print text
    
T = int(readLine())
for caseIndex in xrange(T):
    R,k,N = map(lambda x: int(x), readLine(input).split(" "))
    G = map(lambda x: int(x), readLine(input).split(" "))
    head = 0
    profit = 0
    for r in xrange(R):
        begin = head
        rideSize = 0
        while rideSize+G[head] <= k:
            rideSize += G[head]
            head = (head + 1) % N
            if head == begin:
                break
        profit += rideSize
    writeLine("Case #%d: %d" % (caseIndex+1,profit))