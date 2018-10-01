import sys

class TestCase(object):
  def __init__(self):
    self.numberOfGooglers = -1
    self.numberOfSurprisingScores = -1
    self.minimumInterestingScore = -1
    self.totals = []

    self.numberOfInterestingTotals = 0
    self.usedSurprisingScoresCounter = 0
    
  def run(self):
    for i in range(self.numberOfGooglers):
      total = self.totals[i]
      if self.checkTotalIsInteresting(total):
        self.numberOfInterestingTotals += 1
      
  def checkTotalIsInteresting(self, total):
    interesting = False
    bestUnsurprisingScore = self.getBestUnsurprisingScore(total)
    if bestUnsurprisingScore >= self.minimumInterestingScore:
      interesting = True
    elif self.usedSurprisingScoresCounter < self.numberOfSurprisingScores:
      bestSurprisingScore = self.getBestSurprisingScore(total)
      if bestSurprisingScore >= self.minimumInterestingScore:
        self.usedSurprisingScoresCounter += 1
        interesting = True
    return interesting

  def getUnsurprisingScores(self, total):
    baseScore = int(total / 3)
    remainder = total % 3
    scores = [baseScore, baseScore, baseScore]
    for i in range(len(scores)):
      if remainder == 0:
        break
      else:
        scores[i] += 1
        remainder -= 1
    assert remainder == 0
    assert max(scores) - min(scores) < 2
    return scores
      
  def getBestUnsurprisingScore(self, total):
    return max(self.getUnsurprisingScores(total))
    
  def getSurprisingScores(self, total):
    scores = self.getUnsurprisingScores(total)
    scores.sort()
    #0 0 0 -> -1 0 1   max+=1
    #0 0 1 -> -1 1 1   max+=0
    #0 1 1 ->  0 0 2   max+=1
    remainder = total % 3
    if remainder == 0 and scores[0] > 0:
      scores[0] -= 1
      scores[2] += 1
    elif remainder == 1 and scores[1] > 0:
      scores[0] -= 1
      scores[1] += 1
    elif remainder == 2 and scores[1] > 0:
      scores[1] -= 1
      scores[2] += 1
    assert sum(scores) == total
    return scores

  def getBestSurprisingScore(self, total):
    return max(self.getSurprisingScores(total))
    
def parseTestCaseFromInputLine(testInputLine):
  inputIntegers = map(int, testInputLine.split())    
  test = TestCase()
  test.numberOfGooglers, test.numberOfSurprisingScores, test.minimumInterestingScore = inputIntegers[:3]
  test.totals = inputIntegers[3:]
  return test

if __name__ == '__main__':
  inputFilename = sys.argv[1]
  inputFile = open(inputFilename, 'r')
  inputLines = inputFile.readlines()
  numberOfTests = int(inputLines[0])
  testNumber = 1

  while testNumber <= numberOfTests:
    testInputLine = inputLines[testNumber]
    test = parseTestCaseFromInputLine(testInputLine)

    test.run()
    print 'Case #%s: %s' % (testNumber, test.numberOfInterestingTotals)
    testNumber +=1
    
