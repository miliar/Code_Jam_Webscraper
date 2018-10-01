import sys

def getints():
    return [int(x) for x in sys.stdin.readline().strip().split()]
def getfloats():
    return [float(x) for x in sys.stdin.readline().strip().split()]


T = getints()[0]
for testcase in range(1,1+T):
    farmcost, farmrate, goal = getfloats()

    rate = 2.0
    time = 0.0

    while (goal - farmcost) / rate > goal / (rate + farmrate):
        time += farmcost / rate
        rate += farmrate

    time += goal / rate

    soln = "%f" % time

    print "Case #%d: %s" % (testcase, soln)
