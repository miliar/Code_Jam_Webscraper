with open('input') as f:
    T = int(f.readline())
    for i in range(T):
        s = set([a for a in range(1, 17)])
        for j in range(2):
            c = int(f.readline())
            for k in range(4):
                line  = f.readline()
                if k == c - 1:
                    s = s.intersection([int(x) for x in line.split()])
        if len(s) == 1:
            out = str(s.pop())
        elif len(s) == 0:
            out = "Volunteer cheated!"
        else:
            out = "Bad magician!"
        print "Case #%d: %s" % (i+1, out)
