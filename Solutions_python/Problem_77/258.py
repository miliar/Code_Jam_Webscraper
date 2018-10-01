import sys,math
numOfTests= int(sys.stdin.readline())
for t in range(1,numOfTests+1):
    N = int(sys.stdin.readline())
    init = sys.stdin.readline().split()
    i=1
    ints = [0]*(N+1)
    for j in init:
        ints[i] = int(j)
        i=i+1
         
    swaps = 0.0
    #print ints
    i=1
    while i < len(ints):
        if i != ints[i]:
            swaps= swaps+1
        i=i+1
        #j = ints[i]
        #if i == j:
        #    i = i + 1
        #    continue
        #else swap
        #tmp = ints[j]
        #ints [j] = j
        #ints[i] = tmp
        #swaps = swaps + 2.0
        #print ints
    print "Case #" + str(t) + ": " + str(swaps)

    