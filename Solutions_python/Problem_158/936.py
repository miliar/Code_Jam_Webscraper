for case in range(1, input() + 1):
    X, R, C = map(int, raw_input().split())
    a = ""
    if X < 4:
        if ((R * C) % X == 0 and R * C / X >= 2) or (X, R, C) == (1, 1, 1) or (X, R, C) == (2, 1, 2) or (X, R, C) == (2, 2, 1):
            a = "GABRIEL"
        else:
            a = "RICHARD"
    else:
        if (R * C) % X != 0 or R * C == 4 or (R, C) == (2, 4) or (R, C) == (4, 2):
            a = "RICHARD"
        else:
            a = "GABRIEL"

    print "Case #%d: %s" % (case, a)
