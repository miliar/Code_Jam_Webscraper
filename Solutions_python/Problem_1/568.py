def FindFirstOccurance(sename, qlist):
    for i in range(len(qlist)):
        if(sename == qlist[i]): return i
    return 10000
def saveuniverse(selist, qlist):
    scount = 0
    nqlist = qlist
    while(len(nqlist) > 0):
        maxdist = 0
        for i in range(len(selist)):
            dist = FindFirstOccurance(selist[i], nqlist)
            if(dist > maxdist):
                maxdist = dist
        scount += 1
        nqlist = nqlist[maxdist:]
    if(scount == 0): return 0
    return scount - 1
    
NoOfTestCases = int(raw_input())
for i in range(NoOfTestCases):
    secount = int(raw_input())
    selist = []
    for j in range(secount):
        selist += [raw_input()]
    qcount = int(raw_input())
    qlist = []
    for j in range(qcount):
        qlist += [raw_input()]
    print "Case #%d: %d" % (i+1, saveuniverse(selist, qlist))
