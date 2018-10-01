infile = open("../C-large.in", "r")
outfile = open("../C-large.out", "w")
message = "welcome to code jam"
text = ""
foundCache = {}

def findMessage(msgIndex, textIndex):
    if msgIndex >= len(message):
        return 1
    nOccurrences = 0
    while textIndex < len(text):
        if text[textIndex] == message[msgIndex]:
            if not foundCache.has_key((msgIndex, textIndex)):
                foundCache[(msgIndex, textIndex)] = findMessage(msgIndex + 1, textIndex + 1)
            nOccurrences += foundCache[(msgIndex, textIndex)]
            nOccurrences %= 10000
        textIndex += 1
    return nOccurrences

N = int(infile.readline())
for testcaseN in range(N):
    text = infile.readline().strip()
    foundCache.clear()
    outfile.write("Case #" + str(testcaseN + 1) + ": " + str(findMessage(0, 0)).zfill(4) + "\n")