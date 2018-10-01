

N = int(raw_input())


for case in xrange(N):
    testcase = raw_input().split()[1:]
    t = 0
    Pos = [1,1]
    Last = [0,0]

    
    for  i in xrange(0,len(testcase),2):
        index = 0
        if testcase[i] == "B":
            index = 1
        button = int(testcase[i+1])
        t += 1 + max(0, abs(button-Pos[index]) - (t - Last[index]))
        Last[index] = t
        Pos[index] = button
    print "Case #%d: %d" % (case+1,t)

