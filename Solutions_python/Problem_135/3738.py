import sys

filename = sys.argv[1]

with open(filename, 'r') as f:
    num_cases = int(f.readline().strip())
    for x in xrange(num_cases):
        num_cases -= 1
        row1 = int(f.readline().strip())
        puzzle1 = list()
        for i in xrange(4):
            puzzle1.append(f.readline().strip().split(" "))
        row2 = int(f.readline().strip())
        puzzle2 = list()
        for i in xrange(4):
            puzzle2.append(f.readline().strip().split(" "))
        possibles = list()
        for num in puzzle1[row1-1]:
            if num in puzzle2[row2-1]:
                possibles.append(num)
        if len(possibles) == 1:
            print "Case #" + str(x+1) + ": " + str(possibles[0])
        elif len(possibles) == 0:
            print "Case #" + str(x+1) + ": Volunteer cheated!"
        else:
            print "Case #" + str(x+1) + ": Bad magician!"
