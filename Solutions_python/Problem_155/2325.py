file = open("standingOvation.txt", "r")
lines = file.readlines()
caseNo = int(lines[0])
case = 1
for i in range(1,caseNo + 1):
    caseStr = str()
    standing = 0
    addedPeople = 0
    totalPeople = 0
    a =  (list(lines[i].split()[1]))
    inta = [int(f) for f in a]
    for h in inta:
        totalPeople += h
    
    while (standing < totalPeople):
        for z in inta:
            if (inta.index(z) <= standing):
                standing += int(z)
                inta[inta.index(z)] = 0
        if (standing < totalPeople):
            inta[0] += 1
            addedPeople += 1
            totalPeople += 1
    print("Case #" + str(case) + ": " + str(addedPeople))
    case += 1
