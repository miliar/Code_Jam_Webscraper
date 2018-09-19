import numpy

def parse_cases(infile):
    ret = []
    n = int(infile.readline())
    for i in range(n):
        c = int(infile.readline())
        arr = []
        for j in range(c):
            arr.append(map(float, infile.readline().strip().split()))
        ret.append(arr)
    return ret

def handle_case(case):
    if len(case) == 1:
        return case[0][2]
    def dist(p0,p1):
        return numpy.sqrt(numpy.sum(
                numpy.square([p0[0] - p1[0], p0[1] - p1[1]])))\
                + (p0[2] + p1[2])
    def pairify(l):
        ret = [(ele,ndx) for ndx,ele in enumerate(l)]
        ret.sort()
        return ret[1:]
    def convert(pair):
        dist,ndx = pair
        return (dists[two,ndx], ndx)
    def get_rad(group, ndx):
        if len(group) == 0:
            return case[ndx][2]
        else:
            return group[-1][0]/2
    nplants = len(case)
    dists = numpy.zeros((nplants,nplants))
    for rndx,r in enumerate(case):
        for cndx,c in enumerate(case):
            if rndx != cndx:
                dists[rndx,cndx] = dist(r,c)
    max_spread = numpy.argmax(dists)
    one = max_spread/nplants # row
    two = max_spread % nplants # col
    dists_to_one = pairify(dists[one,:])
    dists_to_two = pairify(dists[:,two])
    # print one,two
    # print dists_to_one
    # print dists_to_two
    best = None
    group1 = dists_to_one[:-1]
    group2 = []
    done = False
    # print dists
    while not done:
        #print [b for a,b in group1] + [one],
        #print [b for a,b in group2] + [two]
        #print len(group1), len(group2), len(case)
        assert len(group1) + len(group2) + 2 == len(case)
        rad1 = get_rad(group1,one)
        rad2 = get_rad(group2,two)
        #print rad1,rad2
        rad = max([rad1,rad2 ])
        if best is None or rad < best:
            best = rad
        if len(group1):
            group2.append(convert(group1[-1]))
            group1.pop()
        else:
            done = True
    return best
    

if __name__ == '__main__':
    import glob
    fname = glob.glob("D-small*.in")[0]
    infile = open(fname)
    cases = parse_cases(infile)
    for ndx,c in enumerate(cases):
        print "Case #%d: %.5f" % (ndx+1, handle_case(c))
