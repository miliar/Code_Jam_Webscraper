trials = int(raw_input())
for i in range(1, trials+1):
    row1 = int(raw_input())

    for x in range(1,5):
        line = raw_input()
        if x==row1:
            set1 = set(line.split())

    row2 = int(raw_input())

    for x in range(1,5):
        line = raw_input()
        if x==row2:
            set2 = set(line.split())

    set3 = set1.intersection(set2)

    if len(set3) == 1:
        y = str(set3.pop())
    elif len(set3) > 1:
        y = "Bad magician!"
    else:
        y = "Volunteer cheated!"

    print "Case #" + str(i) + ": " + y
