from fractions import gcd
outfile = open("outputALarge.txt", "w")

def games(PD):
    return 100/gcd(PD, 100)

linenum = 0
case = 1
for line in open("A-large.in", "rU"):
    if linenum != 0:
        listy = line.strip().split(" ")
        N = int(listy[0])
        PD = int(listy[1])
        PG = int(listy[2])
        if PD < 100 and PG == 100:
            outfile.write("Case #" + str(case) + ": Broken\n")
            case += 1
        elif PD > 0 and PG == 0:
            outfile.write("Case #" + str(case) + ": Broken\n")
            case += 1
        elif games(PD) > N:
            outfile.write("Case #" + str(case) + ": Broken\n")
            case += 1
        else:
            outfile.write("Case #" + str(case) + ": Possible\n")
            case += 1
    linenum += 1

outfile.close()
