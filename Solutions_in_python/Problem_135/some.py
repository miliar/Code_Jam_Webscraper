lines = open("a.in").readlines()
f = open('out.txt', 'w')
for i in xrange(0, int(lines.pop(0))):
    firstAns = int(lines.pop(0)) - 1
    firstLine = [map(lambda x: int(x), lines.pop(0).split(" ")), map(lambda x: int(x), lines.pop(0).split(" ")),
                 map(lambda x: int(x), lines.pop(0).split(" ")), map(lambda x: int(x), lines.pop(0).split(" "))]
    firstLine = map(lambda x: set(x), firstLine)
    secondAns = int(lines.pop(0)) - 1
    secondLine = [map(lambda x: int(x), lines.pop(0).split(" ")), map(lambda x: int(x), lines.pop(0).split(" ")),
                  map(lambda x: int(x), lines.pop(0).split(" ")), map(lambda x: int(x), lines.pop(0).split(" "))]
    secondLine = map(lambda x: set(x), secondLine)

    possiblo = firstLine[firstAns].intersection(secondLine[secondAns])
    num = len(possiblo)
    if num == 1:
        f.write("Case #{0}: {1}\n".format(i+1, possiblo.pop()))
    elif num > 1:
        f.write("Case #{0}: Bad magician!\n".format(i+1))
    else:
        f.write("Case #{0}: Volunteer cheated!\n".format(i+1))

f.close()