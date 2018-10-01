def getinput(filename = ""):
    inputpath = "../input/"
    inpfile = open(inputpath + filename)
    inplist = []
    for line in inpfile:
        line = line.strip()
        if (not line.isdigit()):
            line = line.split(" ")
            inplist.append([ int(line[0]), int(line[1]) ])
    return inplist


inplist = getinput("Recycled Numbers.in")
for l in inplist:
    howmany = 0
    dic = dict()
    for r in range(l[0], l[1] + 1):
        ex = str(r)
        for exi in range(ex.__len__()):
            n = "".join(ex)
            m = ex[exi:] + ex[:exi]
            if (l[0] <= int(n) and int(n) < int(m) and int(m) <= l[1] and len(m) == len(m) and not (n+m) in dic.keys()):
                dic[n+m] = [n,m]
                howmany += 1
                #print "#%d: %d %d %d %d" % (howmany, l[0], int(n), int(m), l[1]) 
    print "Case #%d: %d" % (inplist.index(l) + 1, howmany)
        #print r
        #print "" + str(l[0]) + " " + str(l[1])
        
        
#z = "145"
#for exi in range(1, z.__len__()):
#    exj = z[exi:] + z[:exi]
#    ex = "".join(z)
#    print str(exj) + " " + ex