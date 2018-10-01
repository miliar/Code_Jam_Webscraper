
def solve(timesa, timesb):

    filla = 12*60 - sum((x[1] - x[0] for x in timesa))

    allTimes = timesa + timesb

    sortedTimes = sorted(allTimes, key=lambda x: x[0])

    switches = 0
    sumfilled = 0
    l = len(sortedTimes)
    bigHolesA = []
    bigHolesB = []
    holesSwitch = []

    for i in range(l):

        s = (sortedTimes[(i+1)%l][0] - sortedTimes[i][1]) % (24 * 60)

        if sortedTimes[i][2] != sortedTimes[(i+1)%l][2]:
            holesSwitch.append(s)
        elif sortedTimes[i][2] == 'a':
            bigHolesA.append(s)
        else:
            bigHolesB.append(s)

    holesSwitch = sorted(holesSwitch, reverse=True)
    bigHolesA = sorted(bigHolesA)
    bigHolesB = sorted(bigHolesB, reverse=True)

    for h in bigHolesA:
        if h != 0:
            if h + sumfilled <= filla:
                sumfilled += h
            else:
                sumfilled = filla
                switches += 2

    for h in holesSwitch:
        switches += 1
        if h + sumfilled < filla:
            sumfilled += h
        else:
            sumfilled = filla

    for h in bigHolesB:
        if h != 0:
            if sumfilled < filla:
                sumfilled += h
                switches += 2

    return switches


def main():

    numToCheck = []

    for i in range(int(raw_input())):

        n1, n2 = raw_input().split(' ')
        n1 = int(n1)
        n2 = int(n2)

        timesa = []
        timesb = []

        for i in range(n1):
            s, f = raw_input().split(' ')
            s = int(s)
            f = int(f)
            timesa.append([s,f,'a'])

        for i in range(n2):
            s, f = raw_input().split(' ')
            s = int(s)
            f = int(f)
            timesb.append([s,f,'b'])

        numToCheck.append([timesa, timesb])

    count = 0
    for ta, tb in numToCheck:
        count += 1
        ret = solve(ta, tb)

        print("Case #{}: {}".format(count, ret))


if __name__ == "__main__":
    main()