f = open("in")
T = int(f.readline())

for testcase in xrange(T):
    case = testcase+1

    line = f.readline().strip().split()
    N = int(line[0])
    S = int(line[1])
    p = int(line[2])
    count = 0
    for gn in xrange(N):
        score = int(line[3+gn])
        if score >= 3*p-2:
            count+=1
        elif score >= 3*p-4 and score >= p and S > 0:
            count+=1
            S-=1

    print "Case #%d: %d" % (case, count)
