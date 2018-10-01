inputfile = file("a-small.in", "rb")
outputfile = file("a-small.out", "wb")
out_s = "Case #%d: %s"

parse_line = lambda: [int(a) for a in inputfile.readline().split()]

T = int(inputfile.readline())
for ncase in xrange(1,T+1):
    N, X = parse_line()
    files = parse_line()
    assert len(files) == N
    files.sort()
    count = 0
    disc = []
    while len(files) > 0:
        big = files.pop()
        bigfiles = []
        smallfiles = []
        for file in files:
            if file > X - big:
                bigfiles.append(file)
            else:
                smallfiles.append(file)
        if len(smallfiles) > 0:
            smallfiles.pop()
        files = smallfiles + bigfiles
        count += 1
    print >>outputfile, out_s % (ncase, str(count))
        