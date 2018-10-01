
output = open('output.txt','w')

def readfile(filename):
    first = True
    lineNumber = 0
    with open(filename) as f:
        for line in f:
            
            if first != True:
                lineNumber += 1
                line = line.rstrip()
                if len(line) > 0:
                    lineContent = line.split(" ")
                    #print lineContent
                    output.write("Case #%d: %d\n" % (lineNumber, processCase(int(lineContent[0]),lineContent[1])))
                    #print 
            else:
                first = False

def processCase(maxShyness, numbers):
    required = 0
    sum = 0
    for i in range(0, len(numbers)):
        shyness = i
        shyPeople = int(numbers[i])
        if (sum >= shyness):
            sum += shyPeople
        else:
            needed = shyness - sum
            #print "N:" + str(needed)
            required += needed
            sum += (needed + shyPeople)
    return required

readfile("A-large.in")
output.close()
