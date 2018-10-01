
def TrainTimetable():
    T = int(raw_input())
    NA, NB = map(int, raw_input().split())
    depA, rdyB = parseTimetable(NA, T)
    depB, rdyA = parseTimetable(NB, T)
    print solve(depA, rdyA), solve(depB, rdyB)

def parseTimetable(N, T):
    dep = []
    rdy = []
    for i in range(N):
        sp = raw_input().split()
        dep.append(60 * int(sp[0][0:2]) + int(sp[0][3:5]))
        rdy.append(60 * int(sp[1][0:2]) + int(sp[1][3:5]) + T)
    dep.sort()
    rdy.sort()
    return dep, rdy

def solve(dep, rdy):
    n = 0
    r = 0
    for t in dep:
        if r < len(rdy) and rdy[r] <= t:
            r += 1
        else:
            n += 1
    return n

N = int(raw_input())
for testcase in range(N):
    print "Case #%d:" % (testcase + 1),
    TrainTimetable()
