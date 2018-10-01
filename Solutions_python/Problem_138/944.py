inputfile = file("D-large.in", "rb")
outputfile = file("D-large.out", "wb")
out_s = "Case #%d: %d %d"
parse_line = lambda: [float(a) for a in inputfile.readline().split()]

T = int(inputfile.readline())
for ncase in xrange(1,T+1):
    nblocks = int(inputfile.readline())
    naomi = parse_line()
    ken = parse_line()
    naomi.sort()
    ken.sort()
    
    dwar_pts, war_pts = 0, 0
    
    naomi_copy = naomi[:]
    kcopy = ken[:]
    for i in xrange(nblocks):
        cur = naomi_copy[0]
        for k in kcopy:
            if k > cur:
                kcopy.remove(k)
                naomi_copy.remove(cur)
                break
        else:
            war_pts = len(naomi_copy)
            break
            
    while 1:
        if len(naomi) == 0: break
        if naomi[0] < ken[0]:
            naomi.remove(naomi[0])
            ken.remove(ken[-1])
            if len(naomi) == 0:
                break
        elif naomi[0] > ken[0]:
            naomi.remove(naomi[0])
            ken.remove(ken[0])
            dwar_pts += 1    
            
    print >>outputfile, out_s % (ncase, dwar_pts, war_pts)
    