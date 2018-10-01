# Qualification Round
# Problem A


fname = "A-small-attempt0.in"
f = open(fname,"r")

T = int(f.readline())
for case in range(1,T+1):
    row1 = int(f.readline())
    for j in range(4):
        line = f.readline()
        if j==(row1-1): cards1 = line.split()
    row2 = int(f.readline())
    for j in range(4):
        line = f.readline()
        if j==(row2-1): cards2 = line.split()
    possibles = []
    for c in cards1:
        if c in cards2:
            possibles.append(c)
    if len(possibles)==1:
        print "Case #%i: %s" % (case,possibles[0])
    elif len(possibles)>1:
        print "Case #%i: Bad magician!" % (case)
    else:
        print "Case #%i: Volunteer cheated!" % (case)
