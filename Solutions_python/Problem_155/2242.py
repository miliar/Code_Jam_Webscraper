def standingo(filename):
    file = open(filename)
    filecontents = file.read()
    file.close()

    cases = filecontents.split('\n')

    numcases = int(cases.pop(0))
    #Remove empty line
    cases.pop()
    casenum = 1
    for case in cases:
        length = int(case.split(' ')[0]) + 1
        members = case.split(' ')[1]

        shyindex = 0
        shysum = 0
        guests = 0
        for shyness in members:
            while shysum < shyindex:
                guests += 1
                shysum += 1
            shysum += int(shyness)
            shyindex += 1
        print("Case #{0}: {1}".format(casenum,guests))
        casenum += 1
