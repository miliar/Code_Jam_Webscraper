def isEnoughInAudience(audience):
    standing = audience[0]
    enough = True
    i = 1

    while enough and (i < len(audience)):
        if standing >= i:
            standing += audience[i]
            i += 1
        else:
            enough = False

    return enough

inputFile = raw_input("Enter in path to input file: ")
outputFile = raw_input("Enter in path to output file: ")

fileIn = open(inputFile, "r")
lines = fileIn.readlines()
fileIn.close()

noTests = int(lines[0])
lines.pop(0)

outLines = []

for i in range(noTests):
    line = lines[i].replace("\n", "")

    audience = map(int, list(line.split(' ')[1]))

    originalAudience = sum(audience)

    while not isEnoughInAudience(audience):
        audience[0] += 1

    outLines.append("Case #" + str(i + 1) + ": " + str(sum(audience) - originalAudience))

fileOut = open(outputFile, "w")
fileOut.write("\n".join(outLines))
fileOut.close()