'''
Created on Apr 12, 2014

@author: Miguel Provencio
'''
from sys import stdin

class CaseCount():
    def parseCaseCount(self):
        line = stdin.readline();
        count = int(line)
        self.count = count

    def __str__(self):
        return "Case count: %d" % self.count

class MagicTrick:
    def __init__(self):
        pass
    
    def parseRowCount(self):
        row = stdin.readline().strip()
        return int(row)
    
    def parseCards(self):
        rows = []
        for i in range(4):
            line = stdin.readline().strip()
            cards = line.rsplit(" ")
            rows.append(cards)
        return rows
    
    def getInput(self):
        self.firstRow = self.parseRowCount()
        self.firstCards = self.parseCards()
        self.secondRow = self.parseRowCount()
        self.secondCards = self.parseCards()
        
    def __str__ (self):
        s = ""
        s = s + "First row: %d\n" % self.firstRow
        s = s + "First cards: %s\n" % self.firstCards
        s = s + "Second row: %d\n" % self.secondRow
        s = s + "Second cards: %s\n" % self.secondCards
        s = s + "Answer: %s" % self.answer
        return s
    
    def Calculate(self):
        possibleCards = []
        for x in self.firstCards[self.firstRow-1]:
            for y in self.secondCards[self.secondRow-1]:
                if x == y:
                    possibleCards.append(x)
        
        if len(possibleCards) < 1:
            self.answer = "Volunteer cheated!"
        elif len(possibleCards) == 1:
            self.answer = possibleCards[0]
        elif len(possibleCards) > 1:
            self.answer = "Bad magician!"
            
    def putOutput(self,case):
        print "Case #%d: %s" % (case,self.answer)

if __name__ == "__main__":
    caseCount = CaseCount()
    caseCount.parseCaseCount()
        
    for i in range(caseCount.count):
        magicTrick = MagicTrick()
        magicTrick.getInput()
        magicTrick.Calculate()
        magicTrick.putOutput(i+1)
    
