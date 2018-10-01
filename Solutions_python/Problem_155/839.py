DEBUG = 0
def parseInput(text):
    cases = []
    for i, line in enumerate(text.splitlines()):
        if i == 0:
            continue
        maxShyness, data = line.split(' ')
        people = []
        for char in data:
            people.append(int(char))
        cases.append(people)
    return cases
def getCases(filename):
    with open(filename) as h:
        data = h.read()
    return parseInput(data)

def solveCase(people):
    peopleStood = 0
    peopleAdded = 0
    for shyness, num in enumerate(people):
        DEBUG and print("Starting with #%d: %d people, currently standing %d (added %d)" % (shyness, num, peopleStood, peopleAdded))
        if shyness > (peopleStood + peopleAdded) and num > 0:
            DEBUG and print("Added %d people" % (shyness - peopleStood))
            peopleAdded += shyness - (peopleStood + peopleAdded)
        peopleStood += num
    return peopleAdded

def getOutput(solved):
    lines = []
    for i, solvedCase in enumerate(solved):
        lines.append("Case #%d: %d" % (i + 1, solvedCase))
    return '\n'.join(lines)

def generateOutput(filename, outFile = None):
    cases = getCases(filename)
    #cases = cases[5:6]
    solvedCases = [solveCase(case) for case in cases]
    output = getOutput(solvedCases)
    if outFile == None:
        outFile = filename[:-2] + "out"
    with open(outFile, "w") as h:
        h.write(output)
    
