for T in xrange(input()):
    i = input()-1
    r1 = set(map(int,[raw_input() for _ in xrange(4)][i].split()))
    i = input()-1
    r2 = set(map(int,[raw_input() for _ in xrange(4)][i].split()))
    g = r1&r2
    print "Case #%d:"%(T+1),
    if len(g)==0:
        print "Volunteer cheated!"
    elif len(g)==1:
        print g.pop()
    else:
        print "Bad magician!"
