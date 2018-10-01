def getRow(lines):
  rowNum = int(lines[0])
  return set((int(i) for i in lines[rowNum].split(' ')))
    

lines = open("input.txt").readlines()
outputLines = []
numTests = int(lines.pop(0))
for startingLine in range(0, numTests*10, 10):
    intersection = getRow(lines[startingLine:startingLine+5]) & getRow(lines[startingLine+5:startingLine+10])
    intersectionLength = len(intersection)
    output = "Case #%d: " % ((startingLine/10)+1,)
    if intersectionLength == 1:
      outputLines.append(output + str(list(intersection)[0]) + "\n")
    elif intersectionLength == 0:
      outputLines.append(output + "Volunteer cheated!\n")
    else:
      outputLines.append(output + "Bad magician!\n")

fp = open("output.txt", "w")
fp.writelines(outputLines)
fp.close()