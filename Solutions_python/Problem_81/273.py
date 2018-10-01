cases = int(raw_input())
for case in xrange(cases):
    N = int(raw_input())
    table = [ raw_input() for i in xrange(N)]
    WP = []
    OWP = []
    OOWP = []
    for line in table:
        count = 0
        wins = 0
        for i in line:
            if i == "1":
               count += 1
               wins += 1
            elif i == "0":
                count += 1
        WP.append((wins,count))
    for i in xrange(N):
        count = 0
        total = 0
        for j in xrange(N):
            if table[i][j] == "1":
                average = WP[j][0] / float(WP[j][1]-1)
            elif table[i][j] == "0":
                average = (WP[j][0]-1) / float(WP[j][1]-1)
            else:
                continue
            count += 1
            total += average
        OWP.append((total,count))
    for i in xrange(N):
        total = 0
        count = 0
        for j in xrange(N):
            if table[i][j] != ".":
                total += OWP[j][0] / OWP[j][1]
                count += 1
        OOWP.append(total/count)
    print "Case #%d:" % (case+1)
    for i in xrange(N):
        ans = (WP[i][0]/float(WP[i][1])  )*0.25
        ans2 = 0.5*(OWP[i][0]/OWP[i][1])
        ans3 = 0.25*OOWP[i]
        print "%.6f" % ( ans + ans2 + ans3)




