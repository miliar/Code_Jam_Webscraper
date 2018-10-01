import sys

def myformat(t):
    h, m = [int(x) for x in t.split(":")]
    return h*60+m

def solve(turnaround, timetable):
    ReadyTrain = [[], []]
    AtoB = timetable[0]
    BtoA = timetable[1]
    direction = 0 # 0:A->B, 1: B->A
    result = [0, 0]
    while (len(AtoB) > 0 or len(BtoA) > 0):
        if len(AtoB) > 0 and len(BtoA) > 0:
            if AtoB[0][0] <= BtoA[0][0]:
                direction = 0
            else:
                direction = 1
            depart, arrive = timetable[direction][0]
            result[direction] += 1
            for idx, available_time in enumerate(ReadyTrain[direction]):
                if available_time <= depart:
                    ReadyTrain[direction].pop(idx)
                    result[direction] -= 1
                    break
            ReadyTrain[(direction+1)%2].append(arrive+turnaround)
            timetable[direction].pop(0)
        else:
            if len(AtoB) > 0:
                direction = 0
            else:
                direction = 1
            depart, arrive = timetable[direction][0]
            result[direction] += 1
            for idx, available_time in enumerate(ReadyTrain[direction]):
                if available_time <= depart:
                    ReadyTrain[direction].pop(idx)
                    result[direction] -= 1
                    break
            ReadyTrain[(direction+1)%2].append(arrive+turnaround)
            timetable[direction].pop(0)

    return result

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "usage: %s [inputfile]" % sys.argv[0]
        sys.exit(0)

    fin = open(sys.argv[1])

    case_n = int(fin.readline())
    for i in range(case_n):
        turnaround = int(fin.readline())
        n_ab, n_ba = [int(x) for x in fin.readline().split()]
        AtoB = []
        BtoA = []
        for ab in range(n_ab):
            depart, arrive = [myformat(x) for x in fin.readline().strip().split()]
            AtoB.append((depart, arrive))
        for ba in range(n_ba):
            depart, arrive = [myformat(x) for x in fin.readline().strip().split()]
            BtoA.append((depart, arrive))

        AtoB.sort()
        BtoA.sort()

        a, b = solve(turnaround, [AtoB, BtoA])
        print "Case #%d: %d %d" % (i+1, a, b)
