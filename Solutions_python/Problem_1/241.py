import sys

verbose = False
#iFName = sys.argv[1]
iFName = "d:\projekty\google-jam\universe\A-large.in"

if verbose:
    print "Input file: ", iFName
iFile = open(iFName, "r")

#how many cases?
N = int( iFile.readline())
for i in range(N) :
    switchCnt = 0
    if verbose:
        print i
    #how many search engines?
    S = int( iFile.readline())
    SE = dict()
    #read search engines and set their counters to 0
    for si in range(S) :
        SE[iFile.readline()] = True
    if verbose:
        for si in SE:
            print si, SE[si]
    seLeft = len(SE)
    if verbose:
        print "seLeft = ", seLeft
    Q = int( iFile.readline())
    for qi in range(Q):
        currentSE = iFile.readline()
        if verbose:
            print currentSE, SE[currentSE] 
        if SE[currentSE] :
            SE[currentSE] = False
            seLeft = seLeft - 1
            if seLeft == 0 :
                switchCnt = switchCnt + 1
                for si in SE:
                   SE[si] = True
                   SE[currentSE] = False
                   seLeft = len(SE) - 1

    #if i == N - 1:
    #    print "Case #%(c)d: %(cnt)d" % {'c' : i + 1, 'cnt' : switchCnt},
    #else:
    print "Case #%(c)d: %(cnt)d" % {'c' : i + 1, 'cnt' : switchCnt}
iFile.close()
