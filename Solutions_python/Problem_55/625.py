
def runCoaster(size, gsizes):
    rode = []
    #print "running coaster with %d size" % size
    while (len(gsizes) > 0) and (size >= gsizes[0]):
        #print "letting %d people ride" % gsizes[0]
        rode.append(gsizes[0])
        size -= gsizes[0]
        gsizes = gsizes[1:]
    return rode


def gcjmain3():
    f = file("C-small-attempt1.in", 'r')
    out = file("gcj.out", 'w')
    fs = f.read().split('\n')
    nc = fs[0]
    tot = 0
    for i in range(int(nc)):
        l1 = fs[2*i+1].split(' ')
        l2 = fs[2*i+2].split(' ')
        runs = int(l1[0])
        size = int(l1[1])
        numg = int(l1[2])
        gsizes = [int(x) for x in l2]
        rode = []
        tot = 0
        while runs > 0:
            rode = runCoaster(size, gsizes)
            runs -= 1
            for r in rode:
                tot += int(r)
                gsizes = gsizes[1:]
                gsizes.append(r)
        out.write("Case #%d: %d\n" % (i+1, tot))
        #print "Case #%d: %d" % (i+1, tot)
            

        
