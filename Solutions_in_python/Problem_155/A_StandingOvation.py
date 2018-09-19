import sys

f = open(sys.argv[1])
testcasecount = int(f.readline())

for testcase in range(testcasecount):
    #print("Case #%d:" % (testcase+1))

    testinp = f.readline()[:-1].split(" ")

    #print(testinp)

    Smax = int(testinp[0])
    audience = testinp[1]
    guestcount = 0

    standing = 0
    lvl = 0
    while lvl <= Smax:
        present = int(audience[lvl])
        #print("Level: %d, standing: %d, present:  %d" % (lvl, standing, present))

        if present > 0:
            if standing >= lvl:
                # OK - no need for guests
                standing += present
            else:
                # We need guests
                newguests = lvl-standing
                guestcount += newguests
                standing += newguests + present
                
                #print("Invite %d at level %d" % (newguests, lvl-1))
        lvl += 1

    #print("Total standing: %d" % standing)
    #print("Total guests: %d" % guestcount)

    print("Case #%d: %d" % (testcase+1, guestcount))
