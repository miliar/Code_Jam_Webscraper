import re

inputFilename = "A-small-attempt3.in"

f = open(inputFilename, "r+")

alphabet = list("abcdefghijklmnopqrstuvwxyz")
gAlphabet = list("ynficwlbkuomxsevzpdrjgthaq")

testCase = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
testResult = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"

numLines = int(f.readline())

output = ""

for n, line in enumerate(f):
    result = []
    for i, letter in enumerate(line[:-1]):
        if letter != " ":
            result.append(alphabet[gAlphabet.index(letter)])
        else:
            result.append(" ")
    result = "".join(result)
    output += "Case #" + str(n + 1) + ": " + result + "\n"
    



outputFilename = "output.txt"
outputFile = open(outputFilename, "w")
outputFile.write(output)
outputFile.close()
f.close()

