
file = open("A-small-attempt1.in")

t = file.next()
for test_case in xrange(1, int(t)+1):
    potentials = None

    for spread in xrange(2):
        a = file.next()

        for row_num in xrange(1,5):
            row = set([x.rstrip() for x in file.next().split(" ")])
            if row_num == int(a):
                if potentials is None:
                    potentials = row
                else:
                    potentials = row & potentials

    potentials = list(potentials)

    if len(potentials) == 1:
        result = str(potentials[0])
    elif len(potentials) > 1:
        result = "Bad magician!"
    else:
        result = "Volunteer cheated!"

    print "Case #" + str(test_case) + ": " + result
