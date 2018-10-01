f = open('A.txt')
lines = f.readlines()
f.close()
def find_majority(k):
    myMap = {}
    maximum = ( '', 0 ) # (occurring element, occurrences)
    for n in k:
        if n in myMap: myMap[n] += 1
        else: myMap[n] = 1

        # Keep track of maximum on the go
        if myMap[n] > maximum[1]: maximum = (n,myMap[n])

    return maximum
output = open('AOutput.txt','w')
case = 0
i = 0
while (i < len(lines)-1):
    strings = []
    i += 1
    for j in range(int(lines[i])):
        i += 1
        strings.append(lines[i].split()[0])
        
    output.write("Case #" + str(case+1) + ": ")
    Ostr = []
    for k in range(len(strings)):
        Ostr.append(''.join(sorted(set(strings[k]), key=strings[k].index)))
        
    
    acts = 0
    
    groupstrs = []
    ctr = 0
    for k in range(len(strings)):
        groupstrs.append([])
        ctr2 = 0
        for l in range(len(strings[k])):
            if (l == 0):
                groupstrs[ctr].append(strings[k][0])
            elif(strings[k][l] == strings[k][l-1]):
                groupstrs[ctr][ctr2] += strings[k][l]
            else:
                ctr2 += 1
                groupstrs[ctr].append(strings[k][l])
        ctr += 1
    
    felgawins = 0
    length = len(groupstrs[0])
    for ary in groupstrs:
        if (len(ary) != length):
            felgawins = 1
        
    if (felgawins == 1):
        output.write("Fegla Won")
    else:
        numlets = []
        numct = 0
        for m in range(length):
            numlets.append([])
            for n in range(len(groupstrs)):
                numlets[numct].append(groupstrs[n][m])
            numct += 1
        for o in range(len(numlets)):
            maj = find_majority(numlets[o])
            for x in range(len(numlets[o])):
                acts += abs(len(numlets[o][x]) - len(maj[0]))
            #print [numlets[o], maj[0], maj[1]]
    bob = 0
    for w in range(len(numlets)):
        letter = "".join(set(numlets[w][0]))
        for z in range(len(numlets[0])):
            lett = "".join(set(numlets[w][z]))
            if (letter != lett):
                bob = 1
    if ((bob == 1) and (felgawins != 1)):
        output.write("Fegla Won")
    elif ((felgawins != 1)):
        output.write(str(acts))
    print strings
    print groupstrs
    print numlets
    print acts
    case += 1
    output.write("\n")
output.close() 
