infile = open("A-small-attempt0.in", 'r')
outfile = open("bullseye.out", 'w')
testcases = int(infile.readline())
for s in range(0, testcases):
    r, t = [int(x) for x in infile.readline().split()]
    tmp1 = r*r
    y = 0
    r += 1
    tmp2 = r*r
    while ( t >= tmp2 - tmp1 ):
        t -= tmp2 - tmp1
        y += 1
        r += 1
        tmp1 = r*r
        r += 1
        tmp2 = r*r
    outfile.write("Case #%d: %d\n" % (s+1, y))
infile.close()
outfile.close()
