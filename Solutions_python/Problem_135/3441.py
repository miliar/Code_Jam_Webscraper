f=open("MagicTrickSmall.in",'r+')
cases = f.readline()
for i in xrange(int(cases)):
    row1 = int(f.readline())-1
    arrange1 = []
    for j in xrange(4):
        arrange1.append(f.readline())
    row2 = int(f.readline())-1
    arrange2 = []
    for j in xrange(4):
        arrange2.append(f.readline())
    set1 = arrange1[row1].split()
    set2 = arrange2[row2].split()
    intersect = [val for val in set1 if val in set2]
    if len(intersect) == 0:
        print "Case #" + str(i+1) + ": Volunteer cheated!"
    elif len(intersect) > 1 :
        print "Case #" + str(i+1) + ": Bad magician!"
    else:
        print "Case #" + str(i+1) + ": " + intersect[0]
f.close()

