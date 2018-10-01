import itertools
import math
import operator

class DWTG:
        
    def dancing_with_the_googlers(self):
        inputFile = open('input.txt','r')
        outputFile = open('output.txt','w')
        numTestCases = int(inputFile.readline())
        for tc in range(0,numTestCases):
            line = [int(num) for num in inputFile.readline().split()]
            self.numGooglers = line[0]
            self.numSurprisingCases = line[1]
            self.leastScore = line[2]
            self.maxNumGooglers = 0
            for i in range(3,len(line)):
                self.possibleScores = []
                self.scoreTuples = []
                score = line[i]
                avgScore = score/3
                balanceScore = score - avgScore*3
                scores = [avgScore,avgScore,avgScore]
                index = 0
                while(balanceScore>0):
                    scores[index] += 1
                    balanceScore -= 1
                    index += 1
                    if index%3 == 0:
                        index = 0
                scores = sorted(scores)
                self.computeScores(scores[0],scores[1],scores[2])
                combinations = set(itertools.combinations(scores,2))
                for elem in combinations:
                    s0 = elem[0]
                    s1 = elem[1]
                    s2 = score - (s0+s1)
                
                    s0 = s0 + 1
                    s1 = s1 - 1
                    s2 = s2
                    self.computeScores(s0,s1,s2)
                
                    s0 = s0 - 1
                    s1 = s1 + 1
                    s2 = s2
                    self.computeScores(s0,s1,s2)               
                
                    s0 = s0 - 1
                    s1 = s1 - 1
                    s2 = s2 + 2
                    self.computeScores(s0,s1,s2)
                    
                    s0 = s0 + 1
                    s1 = s1 + 1
                    s2 = s2 - 2
                    self.computeScores(s0,s1,s2)
                for st in self.scoreTuples:
                    isHighScore = st[1]
                    isSurprisingScore = st[2]
                    if isHighScore and not isSurprisingScore:
                        self.maxNumGooglers += 1
                        break
                    elif isHighScore and isSurprisingScore and self.numSurprisingCases != 0:
                        self.maxNumGooglers += 1
                        self.numSurprisingCases -= 1
                        break
                    #print sorted(self.scoreTuples, key=operator.itemgetter(1,2), reverse=True)
            #print self.maxNumGooglers
            outputString = 'Case #%d: %s\n'%(tc+1,self.maxNumGooglers)
            outputFile.write(outputString)
                
    def computeScores(self,s0,s1,s2):
        sortedScores = sorted([s0,s1,s2])
        if self.areScoresValid(s0,s1,s2) and sortedScores not in self.possibleScores:
            self.possibleScores.append(sortedScores)
            surprisingScore = self.areScoresSurprising(s0,s1,s2)
            highScore = self.areScoresHigh(s0,s1,s2,self.leastScore)
            sortedTuple = (sortedScores,highScore,surprisingScore)
            self.scoreTuples.append(sortedTuple)
                
    def areScoresHigh(self,s0,s1,s2,p):
        if s0 >= p or s1 >= p or s2 >= p:
            return True
        else:
            return False

    def areScoresSurprising(self,s0,s1,s2):
        if int(math.fabs(s0-s1))==2 or int(math.fabs(s1-s2))==2 or int(math.fabs(s2-s0))==2:
            return True
        else:
            return False
        
    def areScoresValid(self,s0,s1,s2):
        if s0>=0 and s0<=10 and s1>=0 and s1<=10 and s2>=0 and s2<=10:
            if int(math.fabs(s0-s1))<=2 and int(math.fabs(s1-s2))<=2 and int(math.fabs(s2-s0))<=2:
                return True
            else:
                return False
        else:
            return False
            
if __name__ == '__main__':
    dwtg = DWTG()
    dwtg.dancing_with_the_googlers()