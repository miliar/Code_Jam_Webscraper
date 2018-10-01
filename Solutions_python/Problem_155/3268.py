import sys

def minInvite(line):
    sMax, people = line.split(" ")
    sMax = int(sMax)
    numStanding, count = int(people[0]), 0
    for i in range(1, sMax + 1):
        extra = i - numStanding
        if extra > 0:
            count += extra
            numStanding += extra
        numStanding += int(people[i])
    return count


def run():
    inFile = sys.argv[1]
    lines = [line.strip() for line in open(inFile)]
    T = int(lines[0])

    for i in range(1, T+1):
        numInvited = minInvite(lines[i])
        print("Case #" + str(i) + ": " + str(numInvited))

run()