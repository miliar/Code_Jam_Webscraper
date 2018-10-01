import sys
lines = open(sys.argv[1]).read().strip().split("\n")
numInput = int(lines[0])
for i in range(numInput):
    block = lines[10*i+1:10*(i+1)+1]
    in1 = int(block[0])-1
    in2 = int(block[5])-1
    grid1 = [
            [int(j) for j in block[1].split()],
            [int(j) for j in block[2].split()],
            [int(j) for j in block[3].split()],
            [int(j) for j in block[4].split()]
    ]
    grid2 = [
            [int(j) for j in block[6].split()],
            [int(j) for j in block[7].split()],
            [int(j) for j in block[8].split()],
            [int(j) for j in block[9].split()]
    ]
    out = set(grid1[in1]).intersection(set(grid2[in2]))
    if len(out)==0:
        print "Case #{0}: {1}".format(i+1,"Volunteer cheated!")
    elif len(out)>1:
        print "Case #{0}: {1}".format(i+1,"Bad magician!")
    else:
        print "Case #{0}: {1}".format(i+1,out.pop())
