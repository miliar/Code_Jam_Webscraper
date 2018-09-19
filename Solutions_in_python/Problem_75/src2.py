
class Elements(object):
    def __init__(self):
        self.clearElements()
        
        self.opposedPairs = [] # [("A", "B"), ...]
        self.mixPairs = []  # [(("A", "B"), "C"), ...]
    
    def clearElements(self):
        self.elements = [] # ["A", "B", ...]
        self.counts = {}    # {"A": 0, "B": 3, ... }
        
    def loadProblem(self, line):
        split = line.split(" ")
        numMixPairs = int(split[0])
        
        split = split[1 :]  # I know this is not efficient, but for convenience...
        
        for index in range(numMixPairs):
            threeLetters = split[index]
            assert len(threeLetters) == 3
            (source1, source2, destination) = threeLetters

            self.mixPairs.append(((source1, source2), destination))
            
        numOpposedPairs = int(split[numMixPairs])
        split = split[numMixPairs + 1 :]
        
        for index in range(numOpposedPairs):
            twoLetters = split[index]
            assert len(twoLetters) == 2
            (element1, element2) = twoLetters

            self.opposedPairs.append((element1, element2))
        
        numIncomingElements = int(split[numOpposedPairs])
        split = split[numOpposedPairs + 1 :]
        
        self.incomingElements = split[0]
        assert len(self.incomingElements) == numIncomingElements
        
#        print self.mixPairs
#        print self.opposedPairs
#        print self.incomingElements

    def addElement(self, element):
        """ Append one element without considering the side effect yet """
        self.elements.append(element)
        if element in self.counts:
            self.counts[element] += 1
        else:
            self.counts[element] = 1
        
    def popElement(self):
        """ Pop the last element without considering the side effect yet """
        assert len(self.elements) > 0
        element = self.elements[-1]
        
        self.elements.pop()
        assert self.counts[element] > 0
        
        self.counts[element] -= 1
    
    def applyMixRules(self):
        """ Apply mix rules repeatedly """
        ever = False
        while True:
            applied = False
            for ((source1, source2), destination) in self.mixPairs:
                if self._mixRuleApplies(source1, source2): 
#                    print ((source1, source2), destination)
                    self.popElement()
                    self.popElement()
                    self.addElement(destination)
                    applied = True
                    ever = True
            if not applied:
                break
        return ever

    def _mixRuleApplies(self, source1, source2):
        if len(self.elements) < 2:
            return False
        return ([source1, source2] == self.elements[-2 : ] or 
                [source2, source1] == self.elements[-2 : ])
    
    def applyOpposedRules(self):
        if len(self.elements) >= 2:
            for (element1, element2) in self.opposedPairs:
                if self._getCounts(element1) > 0 and self._getCounts(element2) > 0:
#                    print("%s: cleared due to %s, %s" %
#                          (self.elements, element1, element2))
                    self.clearElements()
                    return
                
    def _getCounts(self, element):
        if element in self.counts:
            return self.counts[element]
        return 0
    
    def invokeElement(self, element):
        self.addElement(element)
        while True:
            ruleApplied = self.applyMixRules()
            if not ruleApplied:
                break
        self.applyOpposedRules()
        
    def dump(self):
        output = "["
        first = True
        for element in self.elements:
            if not first:
                output += ", "
            output += element
            first = False
        output += "]"
        
        return output
        
    
    def solve(self):
        for element in self.incomingElements:
#            print self.elements
            self.invokeElement(element)
#            print self.elements
#            print "---------------------------"
        
        return self.dump()
        
if __name__ == "__main__":
    file = open("e:\\temp\\B-small-attempt0.in")
    numProblems = int(file.readline().strip())
    for i in range(numProblems):
        e = Elements()
        e.loadProblem(file.readline().strip())
        result = e.solve()
        
        print("Case #%d: %s" % (i + 1, result))
    

