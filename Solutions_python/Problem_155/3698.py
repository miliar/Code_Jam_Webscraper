path = "A-small-attempt1.in"
inputFile = open(path, "r")
outputFile = open("output.txt", "w")

T = int(inputFile.readline())
for t in range(0, T):
    shyMax, shyLvls = inputFile.readline().split()

    # Initialize number of standing ppl with Shy Level 0
    standing = int(shyLvls[0])
    extras = 0

    # Iterate over rest of lvls and add to standing if standing >= shyLvl
    for lvl in range(1, int(shyMax) + 1):
        if(int(shyLvls[lvl]) == 0):
            continue
        if(standing >= lvl):
            standing += int(shyLvls[lvl])
        else:
            extras += (lvl - standing)
            standing += (int(shyLvls[lvl]) + extras)

    # print("Case #{0}: {1}".format(t + 1, extras))
    outputFile.write("Case #{0}: {1}\n".format(t + 1, extras))

inputFile.close()
outputFile.close()
