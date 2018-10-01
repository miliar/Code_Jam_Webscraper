infile = open('B-large.in', 'r')
outfile = open('B-large.out', 'w')

for test in range(int(infile.readline())):
    currentline = iter(infile.readline().split())
    newelements = []
    creates = {}
    destroys = []
    #currentline = iter([0, 1, "QW", 2, "QW"])
    for i in range(int(currentline.next())):
        a = currentline.next()
        creates[a[:2]] = a[2:]
        
    for i in range(int(currentline.next())):
        destroys.append(currentline.next())
    
    elements = int(currentline.next())
    elementlist = [i for i in currentline.next()]
    
    for element in elementlist:
        newelements.append(element)
        if len(newelements) > 1:
            if newelements[len(newelements)-1] + newelements[len(newelements)-2] in creates:
                newelements.append(creates[newelements[len(newelements)-1] + newelements[len(newelements)-2]])
                del newelements[len(newelements)-2]
                del newelements[len(newelements)-2]
            elif newelements[len(newelements)-2] + newelements[len(newelements)-1] in creates:
                newelements.append(creates[newelements[len(newelements)-2] + newelements[len(newelements)-1]])
                del newelements[len(newelements)-2]
                del newelements[len(newelements)-2]
            else:
                for possibledestroy in newelements:
                    if possibledestroy + element in destroys:
                        newelements = []
                    elif element + possibledestroy in destroys:
                        newelements = []
    outfile.write("Case #" + str(test+1) + ": " + str(newelements).replace('\'', '') + "\n")