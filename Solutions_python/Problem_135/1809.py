class CardSet:
    # things
    def __init__(self, setOne, setTwo, indOne, indTwo):
        self.setOne = setOne
        self.setTwo = setTwo
        self.indOne = indOne - 1
        self.indTwo = indTwo - 1
    def printMeOut(self):
        print("Index One: " + str(indOne))
        for item in setOne:
            print(item)
        print(" ")
        print ("Index Two: " + str(indTwo))
        for item in setTwo:
            print(item)
    def checkMeOut(self):
        common = [x for x in setTwo[indTwo] for y in setOne[indOne] if x == y]
        #self.printMeOut()
        if len(common) < 1:
            return "Volunteer cheated!"
        elif len(common) > 1:
            return "Bad magician!"
        else:
            return common.pop()
        



infile = open('A-small-attempt0.in', 'r')
outfile = open('out.txt', 'w')

cases = int(infile.readline())
for i in range(1, cases+1):
    indOne = int(infile.readline()) - 1
    setOne = []
    while (len(setOne) < 4):
        row = infile.readline().split()
        setOne.append(row)
    indTwo = int(infile.readline()) - 1
    setTwo = []
    while (len(setTwo) < 4):
        row = infile.readline().split()
        setTwo.append(row)
    cardSet = CardSet(setOne, setTwo, indOne, indTwo)
    outfile.write("Case #" + str(i) + ": " + cardSet.checkMeOut() + "\n")

infile.close()
outfile.close()
