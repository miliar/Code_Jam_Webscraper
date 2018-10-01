FILE = open("B-large.in")
out = open("B-large.out", "w+")

numCases = int(FILE.readline())

for caseNum in range(1,numCases+1):
    line = FILE.readline()
    words = line.split(" ")
    C = float(words[0])
    F = float(words[1])
    X = float(words[2])
    totalTime = 0.0
    totalCookies = 0.0
    prodSpeed = 2
    while (totalCookies < X):
        totalTime += C/prodSpeed
        totalCookies = C
        if (X-C)/prodSpeed > X/(prodSpeed + F):
            totalCookies = 0.0
            prodSpeed += F
        else:
            totalTime += (X-C)/prodSpeed
            totalCookies = X
    #print("Case #" + str(caseNum) + ": " + str(round(totalTime, 7)))
    out.write("Case #" + str(caseNum) + ": " + str(round(totalTime, 7)) + "\n")
out.close()
            
