INPUT_FILE = 'input.txt'
OUTPUT_FILE = 'output.txt'
def mainFunciton():
    inputFile = open(INPUT_FILE, 'r')
    outputFile = open(OUTPUT_FILE, 'w')
    noTestCase = int(inputFile.readline())

    for i in xrange(noTestCase):
        
        #INPUT
        #caseInputCount = inputFile.readline()
        caseInput=inputFile.readline().rstrip('\n').split('/')
        caseInput=[int(x) for x in caseInput]

        #COMPUTATION
        print caseInput
        funOutput = function1(caseInput)

        #OUTPUT
        outputLine =  "Case #" + str(i+1) + ": "
        outputLine += str(funOutput)
        outputFile.write(outputLine + '\n')
    
    inputFile.close()
    outputFile.close()

def function1(caseInput):
    output = 0
    count = 0
    while caseInput[0]/caseInput[1]<1 and output <= 40:
        output += 1
        caseInput[0] = caseInput[0]*2
    
    count = output
    while (caseInput[0]%caseInput[1] != 0) and count <= 40:
        count += 1
        if caseInput[1] <= caseInput[0]:
            caseInput[0] = caseInput[0] - caseInput[1]
        caseInput[0] = caseInput[0] * 2
    
    if count > 40:
        output = "impossible"
    return output

if __name__ == '__main__':
    mainFunciton()