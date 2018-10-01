INPUT_FILE = r'D:\Downloads\FromChrome\A-small-attempt0.in'
OUTPUT_FILE = r'D:\Assaf\Fun\GoogleCodeJam2012\A-small-attempt0.out'

inputFile = file(INPUT_FILE, 'rb')
numQuestions = int(inputFile.readline())
outputFile = file(OUTPUT_FILE, 'wb')

def solveQuestion(x):
    d = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}
    result = ''
    for c in x:
        if c in d:
            result += d[c]
        else:
            if c != '\n' and c != '\r':
                result += c
    return result

for q in xrange(numQuestions):
    outputFile.write("Case #%d: " % (q+1))
    # Don't forget to read length of a list
    x = inputFile.readline()
    result = solveQuestion(x)
    outputFile.write(result)
    outputFile.write("\n")

outputFile.close()
inputFile.close()
# print file(OUTPUT_FILE, 'rb').read()

