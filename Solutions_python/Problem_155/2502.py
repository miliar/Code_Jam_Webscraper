def run_prog(j):
    SMax, ShyList = raw_input().split()
    SMax = int(SMax)

    ShyListInt =  [int(x) for x in ShyList]

    ExtraPeople = 0
    RunningCount = 0
    for i in xrange(SMax+1):
        RunningCount = RunningCount + ShyListInt[i]
        if(not(RunningCount > i)):
            ExtraPeople = ExtraPeople + 1
            RunningCount = RunningCount + 1
    print "Case #{}: {}".format(j, ExtraPeople)

iters = int(raw_input())
[run_prog(j+1) for j in xrange(iters)]
