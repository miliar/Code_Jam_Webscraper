filename = "tmp.txt"

f = open(filename)

amount_tests = int(f.readline())

test = 0
while test < amount_tests:
    test += 1
    answ_1 = int(f.readline())
    for i in xrange(4):
        if i + 1 == answ_1:
            row_1 = set([int(j) for j in f.readline().split()])
        else:
            f.readline()
    answ_2 = int(f.readline())
    for i in xrange(4):
        if i + 1 == answ_2:
            row_2 = set([int(j) for j in f.readline().split()])
        else:
            f.readline()
    answ = list( row_1 & row_2 )

    if len(answ) == 1:
         print "Case #{}: {}".format(test , answ[0])
    elif len(answ) > 1:
        print "Case #%d: Bad magician!" % test
    elif len(answ) == 0:
        print "Case #%d: Volunteer cheated!" % test
    pass