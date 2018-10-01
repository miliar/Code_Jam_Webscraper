__author__ = 'PrimuS'

f = open("d:\\dev\\acm\\codeJam 2015\\D-small-attempt1.in", "r")
of = open("d:\\dev\\acm\\codeJam 2015\\D_res_small.txt", "w")

T = int(f.readline())

for t in range(1, T + 1):
    x,r,c = [int(x) for x in f.readline().split()]
    res = True
    if x == 1:
        res = True
    if x == 2:
        if (r * c) % 2 != 0:
            res = False

    if x == 3:
        if r < 3 and c < 3:
            res = False
        elif (r == 3 or c == 3):
            if r * c == 3:
                res = False
        else:
            res = False
    if  x == 4:
        if r < 4 and c < 4:
            res = False
        elif r * c < 12:
            res = False

    if res:
        res = "GABRIEL"
    else:
        res = "RICHARD"
    print("Case #{:d}: {:s}".format(t, res), file=of)

of.close()
