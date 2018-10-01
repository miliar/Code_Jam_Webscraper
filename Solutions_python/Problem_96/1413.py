fin = file("B-large(1).in", "rU")
fout = file("B-large.out", "w")

nruns = int(fin.readline().strip())
for i in xrange(nruns):
    line = fin.readline().strip().split()
    ngoog = int(line[0])
    nsurp = int(line[1])
    bestres = int(line[2])
    googpoints = [int(x) for x in line[3:]]
    nsurpscore = []
    surpscore = []
    boolarray = []
    #print googpoints
    for x in googpoints:
        bestnsurp = x/3
        if x == 0:
            bestnsurp = 0
        elif x == 1:
            bestnsurp = 1
        elif x % 3 != 0:
            bestnsurp += 1
        nsurpscore.append(bestnsurp)
        bestsurp = x/3
        if x == 0:
            bestsurp = 0
        elif x == 1:
            bestsurp = 1
        elif x == 2:
            bestsurp = 2
        elif x % 3 == 0 or x % 3 == 1:
            bestsurp += 1
        else:
            bestsurp += 2
        surpscore.append(bestsurp)
        boolarray.append(0)
    #pick nonsurprising above p
    for j in xrange(ngoog):
        if nsurpscore[j] >= bestres:
            boolarray[j] = 1
    for j in xrange(ngoog):
        if nsurp == 0:
            break
        if boolarray[j] == 0 and surpscore[j] >= bestres:
            boolarray[j] = 1
            nsurp -= 1
    #print nsurpscore
    #print surpscore
    #print boolarray
    #print
    
    strout = "Case #" + str(i+1) + ": " + str(sum(boolarray)) + "\n"
    #print strout
    fout.write(strout)
fin.close()
fout.close()
