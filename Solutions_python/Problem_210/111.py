import sys

def next_line():
    return input_file.readline().rstrip()

input_file = open(sys.argv[1])
for case in range(1, int(next_line())+1):
    print "Case #%s:" % (case),
    C, J = map(int, next_line().split())
    AC = []
    AJ = []
    for i in xrange(C):
        AC.append(map(int, next_line().split())+["C"])
    for i in xrange(J):
        AJ.append(map(int, next_line().split())+["J"])
    activities = sorted(AC + AJ)
    #print activities
    START, END, PERSON = range(3)
    prev = activities[-1]
    contiguous = {"C": [], "J": []}
    left = {"C": 720, "J": 720}
    switch = 0
    for activity in activities:
        if prev[PERSON] == activity[PERSON]:
            gap = (activity[START] - prev[END]) % (720*2)
            contiguous[activity[PERSON]].append(gap)
        else:
            switch += 1
        left[activity[PERSON]] -= activity[END] - activity[START]
        prev = activity
    #print switch
    #print contiguous
    #print left
    split = {}
    for person in "CJ":
        contiguous[person].sort()
        partial = 0
        count = 0
        for gap in contiguous[person]:
            if partial + gap > left[person]:
                break
            count += 1
        split[person] = len(contiguous[person]) - count
    print switch + (split["C"] + split["J"]) * 2
