f = open("data.txt", 'r')
g = open("data1.txt", 'w')
t = int(f.readline())
for i in range(t):
    answer1 = int(f.readline())
    for j in range(4):
        if j == answer1 - 1:
            firstset = set([int(x) for x in f.readline().split()])
        else:
            f.readline()
    answer2 = int(f.readline())
    for j in range(4):
        if j == answer2 - 1:
            secondset = set([int(x) for x in f.readline().split()])
        else:
            f.readline()
    intersection = list(firstset & secondset)
    if len(intersection) == 1:
        g.write("Case #%d: %d\n" % (i+1, intersection[0]))
    elif len(intersection) == 0:
        g.write("Case #%d: Volunteer cheated!\n" % (i+1))
    else:
        g.write("Case #%d: Bad magician!\n" % (i+1))
f.close()
g.close()