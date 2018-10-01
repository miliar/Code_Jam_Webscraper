Matrix1 = [[0 for x in xrange(4)] for x in xrange(4)]
Matrix2 = [[0 for x in xrange(4)] for x in xrange(4)]

fxs = open("C:\Users\Petr\Downloads\A-small-attempt2.in", "r")

repeat = int(fxs.readline())

for count in range(repeat):
######repeat this####

    row1 = int(fxs.readline())

    for x in range(4):
        line = fxs.readline()
        for y in range(4):
            Matrix1[x][y] = line.split()[y]



    row2 = int(fxs.readline())

    for x in range(4):
        line = fxs.readline()
        for y in range(4):
            Matrix2[x][y] = line.split()[y]


    common = list(set(Matrix1[row1 - 1]).intersection(Matrix2[row2 - 1]))

    if len(common) > 1:
        output = "Bad magician!"
    elif len(common) == 0:
        output = "Volunteer cheated!"
    else: output = str(common[0])

    lst = ["Case #", str(count + 1), ": ", output]
    print  "".join(lst)
