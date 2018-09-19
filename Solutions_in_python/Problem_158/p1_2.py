
cases = int(raw_input())
for case in range(cases):
    line1 = raw_input().split()
    X = int(line1[0])
    R = int(line1[1])
    C = int(line1[2])
    print "Case #%s:" % (case+1),
    if (X > R) and (X > C):
        print "RICHARD"
        continue
    if X == 1:
        print "GABRIEL"
        continue
    if X == 2:
        if R == 1 and C == 3:
            print "RICHARD"
            continue
        if R == 3 and C == 1:
            print "RICHARD"
            continue
        if R == 3 and C == 3:
            print "RICHARD"
            continue
        print "GABRIEL"
        continue
    if X == 3:
        if R == 1 and C == 3:
            print "RICHARD"
            continue
        if R == 3 and C == 1:
            print "RICHARD"
            continue
        if R == 1 and C == 4:
            print "RICHARD"
            continue
        if R == 4 and C == 1:
            print "RICHARD"
            continue
        if R == 4 and C == 2:
            print "RICHARD"
            continue
        if R == 2 and C == 4:
            print "RICHARD"
            continue
        if R == 4 and C == 4:
            print "RICHARD"
            continue
        print "GABRIEL"
        continue
    if X == 4:
        if R==4 and C==4:    
            print "GABRIEL"
            continue
        if R==3 and C==4:
            print "GABRIEL"
            continue
        if R==4 and C==3:
            print "GABRIEL"
            continue
        print "RICHARD"
        continue

















