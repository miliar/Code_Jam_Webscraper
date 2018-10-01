def loadWords():
    inFile = open('D-small-attempt0.in', 'r', 0)
    line = inFile.readlines()
    numLines = line.pop(0)
    line = [x.strip('\n') for x in line]
    temp = []
    for i in xrange(int(numLines)):
        temp.append(line[:3])
        line = line[3:]
        
    return temp, int(numLines)

def writeWords(lst):
    out = open('D-small-attempt0.out', 'w')
    count = 0
    for i in lst:
        count +=1
        out.write('Case #%d: ' %count + str(i) +'\n')
        
load, number = loadWords()

def cheat_fun(naomi,ken):
    naomi1 = naomi[:]
    ken1 = ken[:]
    while True:
        count = 0
        for i,j in zip(naomi1,ken1):
            if i < j:
                naomi1.remove(i)
                ken1 = ken1[:-1]
                break
            count += 1
        if count == len(naomi1):
            break
    return len(naomi1)

def normal_fun(naomi,ken):
    normal = 0
    naomi2 = naomi[:]
    ken2 = ken[:]
    for log in naomi2[::-1]:
        if ken2[-1] < log:
            normal += 1
            ken2 = ken2[1:]
        else:
            index = ken2[-1]
            for i in ken2[::-1]:
                if i < log:
                    ken2.remove(index)
                    break
                index = i
    return normal


cheat_list = []
for game in load:
    numItems = int(game[0])
    naomi = [float(x) for x in game[1].split(' ')]
    ken = [float(x) for x in game[2].split(' ')]
    naomi = sorted(naomi)
    ken = sorted(ken)
    cheat = cheat_fun(naomi,ken) #cheating
    normal = normal_fun(naomi,ken) #not cheating
    cheat_list.append(str(cheat) + ' ' + str(normal))
#    print str(cheat) + ' ' + str(normal)
writeWords(cheat_list)