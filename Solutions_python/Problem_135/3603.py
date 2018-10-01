__author__ = 'tivvit'

f = open('A-small-attempt0.in')
outf = open('output.out', 'w')

cases = int(f.readline())
runnedCases = 1
while runnedCases <= cases:
    #row1 = input() - 1
    row1 = int(f.readline()) - 1
    mat1 = [[] for i in range(4)]
    for x in range(0, 4):
        mat1[x] = [int(i) for i in f.readline().split()] #raw_input()
    #print mat1
    row2 = int(f.readline()) - 1
    mat2 = [[] for i in range(4)]
    for x in range(0, 4):
        mat2[x] = [int(i) for i in f.readline().split()]
    #print mat2
    #print set(mat1[row1])
    #print set(mat2[row2])
    found = list(set(mat1[row1]) & set(mat2[row2]))
    length = len(found)

    out = "Case #" + str(runnedCases) + ": "

    if length == 1:
        out += str(found[0])
    elif length > 1:
        out += str("Bad magician!")
    else:
        out += str("Volunteer cheated!")

    print out
    outf.write(out + '\n')

    runnedCases += 1

f.close()
outf.close()