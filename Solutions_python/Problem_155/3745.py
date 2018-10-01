def subprocess(i, rest, cumsum, added):
    # print "%s, %s, %s, %s" % (i, rest, cumsum, added)
    si = int(rest[0])
    newly_added = 0
    if cumsum < i:
        newly_added = i - cumsum
    if len(rest) == 1:
        # print "Returning " + str(added + newly_added)
        return added + newly_added
    else:
        return subprocess(i+1, rest[1:], cumsum + si + newly_added, added + newly_added)

f = open("A-small-attempt0.in", 'r')
out = open("out", "w")
testcases = int(f.readline())
for i in range(testcases):
    line = f.readline()
    n, s = line.split(" ")
    # print process(s)
    out.write("Case #%d: %s\n" % (i+1, subprocess(0, s[:-1], 0, 0)))
    # if len(a) == 0:
    #     print "Case #%d: Volunteer cheated!" % (i+1)
    # elif len(a) == 1:
    #     print "Case #%d: %d" % (i+1, a.pop())
    # else:
    #     print "Case #%d: Bad magician!" % (i+1)
