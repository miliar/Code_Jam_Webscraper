print("Input file:")

fname = input()
print("Opening " + fname + ".in")
fin = open(fname + ".in")
lines = fin.readlines()
T = lines[0]
i = 1
fout = open(fname + ".out", "w")
while (i < len(lines)):
    fout.write("Case #" + str(int((i-1)/10 + 1)) + ": ")
    rowA = int(lines[i])
    cardsA = [int(j) for j in lines[i+rowA].split(" ")]
    i += 5
    rowB = int(lines[i])
    cardsB = [int(j) for j in lines[i+rowB].split(" ")]
    possibilities = list(set(cardsA).intersection(set(cardsB)))
    if len(possibilities) > 1:
        fout.write("Bad magician!\n")
    if len(possibilities) < 1:
        fout.write("Volunteer cheated!\n")
    if len(possibilities) == 1:
        fout.write(str(possibilities[0]) + "\n" )
    i += 5
fout.close()
