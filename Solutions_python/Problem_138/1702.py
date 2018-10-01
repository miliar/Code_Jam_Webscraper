__author__ = 'Drazen'
import bisect


def getScores(naomi, kenRegular):
    kenDeceitful = list(kenRegular)
    warScore = 0
    deceitfulWarScore = 0
    for i, naomisBlock in enumerate(naomi):
        #regular war
        greaterBlockIndex = bisect.bisect(kenRegular, naomisBlock)
        if greaterBlockIndex < len(kenRegular):
            del(kenRegular[greaterBlockIndex])
        else:
            del(kenRegular[0])
            warScore += 1
        #deceitful war
        if naomisBlock < kenDeceitful[0]:
            del(kenDeceitful[-1])
        else:
            del(kenDeceitful[0])
            deceitfulWarScore += 1
    return [deceitfulWarScore, warScore]



if __name__ == "__main__":
    inputFile = open('H:/development/GoogleCodeJam/2014/D/D-large.in', mode='r')
    outputFile = open('H:/development/GoogleCodeJam/2014/D/output.txt', mode='w')
    resultLine = 'Case #{0}: {1} {2}'
    inputFile.seek(0)
    numberOfTests = int(inputFile.readline())
    for i in range(numberOfTests):
        N = int(inputFile.readline())
        naomi = map(float, inputFile.readline().split())
        naomi.sort()
        ken = map(float, inputFile.readline().split())
        ken.sort()
        scores = getScores(naomi, ken)
        outputFile.write(str.format(resultLine, i+1, scores[0], scores[1]) + '\n')
    inputFile.close()
    outputFile.close()