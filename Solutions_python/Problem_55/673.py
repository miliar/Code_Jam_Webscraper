#Filename: ThemePark.py

infile = open("C-small.in")
outfile = open("output.txt",'w')

cases = int(infile.readline())

for i in range(1, cases+1):
    temp = (infile.readline()).split()
    runs = int(temp[0])
    size = int(temp[1])
    numGroups = int(temp[2])
    money = 0

    groups = (infile.readline()).split()

    for each in range(0, len(groups)):
        lala = groups[each]
        groups[each] = int(lala)

    while runs > 0:
        fill = 0
        used = 0
        while (fill + groups[0]) <= size and used < numGroups:
            fill += groups[0]
            groups.append(groups.pop(0))
            used += 1
        money += fill
        runs -= 1

    outfile.write("Case #{0}: {1}\n".format(i, money))

infile.close()
outfile.close()
