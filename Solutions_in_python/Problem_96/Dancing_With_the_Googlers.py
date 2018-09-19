import os

inputFilename = os.path.splitext(os.path.basename(__file__))[0]+".in"
inputFile = open(inputFilename,"r")

outputFilename = os.path.splitext(os.path.basename(__file__))[0]+".out"
outputFile = open(outputFilename,"w")


sampleNum = int(inputFile.readline().strip())
lstSample = []

for i in range(sampleNum):
    numQualify = 0
    inputLine = map(lambda x:int(x), inputFile.readline().strip().split(" "))
    numGoogler, s, p  =  inputLine[:3]
    lstScores = inputLine[3:]
    print numGoogler, s, p,lstScores
    if p == 0:
        numQualify = numGoogler
    else:
        minScore =  p*3-2
        goodScores = [x for x in lstScores if x >= minScore]
        badSocres = [x for x in lstScores if x < minScore]

        if len(goodScores) == len(lstScores):
            for score in goodScores:
                if score >= p:
                    numQualify += 1
        else:
            for score in goodScores:
                if score >= p:
                    numQualify += 1
                    
            for score in badSocres:
                if s > 0 and score >= p and score >= p*3-4:
                    numQualify += 1
                    s -= 1            

    resultLine ="Case #%s: %s"%(i+1,numQualify)+"\n"
    print resultLine
    outputFile.write(resultLine)
outputFile.close()