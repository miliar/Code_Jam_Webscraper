infile = open("B-large.in", "r")
outfile = open("outfile", "a")

lines = infile.readlines()
a = 0
e = -1

for line in lines:

    c = 0
    d = 0
    total = 0
    rate = 2
    C = 0
    F = 0
    X = 0
    e += 1

    if a == 0:
        b = int(line[:-1])
        a += 1

    else:
        for j in range(len(line)):
            if line[j] == " " and c == 0 and d == 0:
                C = float(line[:j])
                c = j + 1
            elif line[j] == " " and d == 0:
                F = float(line[c:j])
                d = j + 1
        X = float(line[d:])

        while True:
            if X / rate > ((X / (rate + F)) + C / rate):
                total += C / rate
                rate += F
            else:
                total += (X / rate)
                break

        outfile.write("Case #" + str(e) + ": " + "{0:.7f}".format(total))
        outfile.write("\n")

infile.close()
outfile.close()
