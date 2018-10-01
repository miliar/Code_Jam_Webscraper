fin = open("magic.in", "r")
fout = open("output.txt", "w")
file = fin.read().split("\n")
file.pop(0)
linenum = 0
case = 1
innum = 1
print (file)
for line in (file):
    result = []
    if linenum == 0:
        position = int(line)
        case = 1
    elif 0 < linenum < 5:
        if position == case:
            com1 = line.split()
        case += 1
    elif linenum == 5:
        position2 = int(line)
        case = 1
    else:
        if position2 == case:
            com2 = line.split()
            for i in com1:
                if i in com2:
                    result.append(i)
            fout.write("Case #%d: " %innum)
            innum += 1
            print (result)
            if len(result) > 1:
                fout.write("Bad magician!")
            elif result:
                fout.write(result[0])
            else:
                fout.write("Volunteer cheated!")
            fout.write("\n")
        case += 1
    linenum += 1
    linenum %= 10
fout.close()
fin.close()
