casenumber = 1
file = open("C-small-attempt0.in")
wfile = open("2.txt", "w")
numberofcases = int(file.readline()) +1

while casenumber < numberofcases:
    line = file.readline()
    
    if not line:
        break
    numbers = line.split()
    R = int(numbers[0])
    
    k = int(numbers[1])
    N = int(numbers[2])
    line = file.readline()
    if not line:
        break
    groups = []   
    a = line.split()
    for numbers in a:
        groups.append(int(numbers))
    
    riddentoday = 0
    totalcash = 0

    while riddentoday < R:
        rollercoaster = [] 
        for x in range(len(groups)):
            if (groups[0] + sum(rollercoaster)) > k: 
                break
            else:
                rollercoaster.append(groups[0])
                groups.append(groups.pop(0))
        totalcash += sum(rollercoaster)
        riddentoday += 1
    wfile.writelines("Case #" + str(casenumber) + ": " + str(totalcash) + "\n")
    casenumber+=1
wfile.close()
