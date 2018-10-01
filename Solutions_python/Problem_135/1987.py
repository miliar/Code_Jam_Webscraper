import sys

infile = open(sys.argv[1])
outfile = open("magic_trick_out", "w")

number = infile.readline().strip()
number = int(number)

for i in range(number):
    row = infile.readline().strip()
    row = int(row)
    for j in range(4):
        line = infile.readline()    
        if j+1 == row :
            first = [int(k) for k in line.split()]

    row2 = infile.readline().strip()
    row2 = int(row2)
    for j in range(4):
        line = infile.readline()
        if j+1 == row2 :
            second = [int(k) for k in line.split()]

    intersection = list(set(first) & set(second))

    case = "Case #" + str(i+1) + ": "
    if len(intersection) == 1:
        outfile.write(case + str(intersection[0]) + "\n")
    elif len(intersection) == 0:
        outfile.write(case + "Volunteer cheated!\n")
    else:
        outfile.write(case + "Bad magician!\n")

