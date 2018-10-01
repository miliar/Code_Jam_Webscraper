import sys

if len(sys.argv) == 1:
    print("No input file provided.")
    sys.exit()
else:
    filename = sys.argv[1]
    try:
        fileobject = open(filename, 'r')
    except:
        print("Failed to open given file.")
        sys.exit()
    try:
        firstLine = fileobject.readline()
    except:
        print("Failed to read first line.")
        sys.exit()
    datasetSize = int(firstLine)
    if not datasetSize:
        print("Unable to parse dataset size.")
        sys.exit()
    lineNr = 1
    for i in range(datasetSize):
        lineNr = lineNr + 1
        try:
            lineText = fileobject.readline()
        except:
            print("Failed to read line ", lineNr)
            sys.exit()
        textToParse = lineText.strip()
        inputParams = textToParse.split(" ")
        [N, R, O, Y, G, B, V] = map(int, inputParams)
        horses = {"N": N, "R": R, "O": O, "Y": Y, "G": G, "B": B, "V": V}
        output = ""
        impossible = False
        fragments = []
        # It's not possible to put horses with 2-color manes next to each other.
        # That's 2 manes with 4 colors total, but there are only 3 colors
        # available.
        for [colorSingle, colorMixed] in [["R", "G"], ["Y", "V"], ["B", "O"]]:
            if horses[colorSingle] + horses[colorMixed] == N:
                if horses[colorSingle] != horses[colorMixed]:
                    impossible = True
                    break
                fragments.append((colorSingle + colorMixed) * horses[colorMixed])
                horses[colorSingle] -= horses[colorMixed]
                horses[colorMixed] = 0
            else:
                if horses[colorSingle] + 1 < horses[colorMixed]:
                    impossible = True
                    break
                if horses[colorMixed] > 0:
                    fragments.append((colorSingle + colorMixed) * horses[colorMixed] + colorSingle)
                    horses[colorSingle] -= horses[colorMixed] - 1
                    horses[colorMixed] = 0
                else:
                    fragments.append("")
        if not impossible:
            if horses["B"] > horses["R"] + horses["Y"]:
                if horses["B"] == horses["R"] + horses["Y"] + 1 and fragments[0] != "" and fragments[1] != "":
                    fragments[0] = fragments[0] + "B"
                    horses["B"] -= 1
                else:
                    impossible = True
            elif horses["R"] > horses["B"] + horses["Y"]:
                if horses["R"] == horses["B"] + horses["Y"] + 1 and fragments[1] != "" and fragments[2] != "":
                    fragments[1] = fragments[1] + "R"
                    horses["R"] -= 1
                else:
                    impossible = True
            elif horses["Y"] > horses["B"] + horses["R"]:
                if horses["Y"] == horses["B"] + horses["R"] + 1 and fragments[2] != "" and fragments[0] != "":
                    fragments[2] = fragments[2] + "Y"
                    horses["Y"] -= 1
                else:
                    impossible = True
        if not impossible:
            output = fragments[0] + fragments[1] + fragments[2]
            while sum([horses["R"], horses["Y"], horses["B"]]) > 0:
                if output == "":
                    for color in ["R", "Y", "B"]:
                        if horses[color] == max(horses["R"], horses["Y"], horses["B"]):
                            output = color
                            horses[color] = horses[color] - 1
                            break
                else:
                    lastColor = output[-1]
                    firstColor = output[0]
                    colorsAvailable = set(["R", "Y", "B"]) - set([lastColor])
                    for color in colorsAvailable:
                        if firstColor in colorsAvailable and horses[firstColor] == horses[list(colorsAvailable - set([firstColor]))[0]]:
                            output += firstColor
                            horses[firstColor] = horses[firstColor] - 1
                        else:
                            if horses[color] == max([horses[color2] for color2 in colorsAvailable]):
                                output += color
                                horses[color] = horses[color] - 1
                                break
        else:
            output = "IMPOSSIBLE"
        if i == 0:
            startCharacter = ""
        else:
            startCharacter = "\n"
        print(startCharacter, "Case #", i+1, ": ", output, end="", sep="")