

def switchLetter(o):
    if o == 'y':
        return 'a'
    elif o == 'n':
        return 'b'
    elif o == 'f':
        return 'c'
    elif o == 'i':
        return 'd'
    elif o == 'c':
        return 'e'
    elif o == 'w':
        return 'f'
    elif o == 'l':
        return 'g'
    elif o == 'b':
        return 'h'
    elif o == 'k':
        return 'i'
    elif o == 'u':
        return 'j'
    elif o == 'o':
        return 'k'
    elif o == 'm':
        return 'l'
    elif o == 'x':
        return 'm'
    elif o == 's':
        return 'n'
    elif o == 'e':
        return 'o'
    elif o == 'v':
        return 'p'
    elif o == 'z':
        return 'q'
    elif o == 'p':
        return 'r'
    elif o == 'd':
        return 's'
    elif o == 'r':
        return 't'
    elif o == 'j':
        return 'u'
    elif o == 'g':
        return 'v'
    elif o == 't':
        return 'w'
    elif o == 'h':
        return 'x'
    elif o == 'a':
        return 'y'
    elif o == 'q':
        return 'z'
    else:
        return o
    

def translate(caseNum, googLine):
    transLine = ""
    
    for x in range(len(googLine)-1):
        transLine += switchLetter(googLine[x])

    return "Case #%d: %s" % ((caseNum+1), transLine)

def main():
    inputFile = open("/home/brenton/Development/codeJam/input", 'r')
    numLines = inputFile.readline()
    numLines = numLines[0:(len(numLines)-1)]

    outputFile = open("/home/brenton/Development/codeJam/output", 'w')
    
    for x in range(int(numLines)):
        googLine = inputFile.readline()
        engLine = translate(x, googLine)
        outputFile.write(engLine+"\n")


if __name__ == "__main__":
    main()
