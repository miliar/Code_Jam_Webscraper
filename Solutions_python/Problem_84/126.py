outfile = open("outputA.txt","w")
linenum = 0
stat = "coords"
case = 1
for line in open("A-small-attempt0.in", "rU"):
    if linenum != 0:
        if stat == "coords":
            stat = "grid"
            listy = line.strip().split(" ")
            rows = int(listy[0])
            columns = int(listy[1])
            counter = 0
            current = []
            finishgrid = []
            status = "possible"
        elif stat == "grid":
            if status == "possible":
                sortrow = list(line.strip())
                editrow = ""
                index = 0
                newcurrent = []
                while index < columns:
                    if index in current:
                        if sortrow[index] != "#" or sortrow[index+1] != "#":
                            status = "impossible"
                            break
                        else:
                            editrow = editrow + "\\/"
                            index += 2
                    elif sortrow[index] == ".":
                        editrow = editrow + "."
                        index += 1
                    elif sortrow[index] == "#":
                        if index == columns - 1 or sortrow[index + 1] != "#":
                            status = "impossible"
                            break
                        else:
                            newcurrent.append(index)
                            editrow = editrow + "/\\"
                            index += 2
                print current, newcurrent, case
                current = newcurrent
                finishgrid.append(editrow)
            counter += 1
            if counter == rows:
                stat = "coords"
                if status == "impossible":
                    outfile.write("Case #" + str(case) + ":\nImpossible\n")
                else:
                    outfile.write("Case #" + str(case) + ":\n" + "\n".join(finishgrid) + "\n")
                case += 1
    linenum += 1
outfile.close()
