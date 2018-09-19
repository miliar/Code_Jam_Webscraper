
def finder (data):
    data = [int(x) for x in data.split()]
    X = data[0]

    C = data[2]
    R = data[1]
    lol = R * C

    if X >= 7:
        return "RICHARD"
    elif X == 1:
        return "GABRIEL"
    elif X == 2:
        if (lol % 2 == 0) :
            return "GABRIEL"
        else:
            return "RICHARD"
    elif X == 3:
        if (R == 1) or (C == 1) or (lol % 3 != 0):
            return "RICHARD"
        else:
            return "GABRIEL"

    elif X == 4:
        if (lol % 4 != 0 ) or (R < 3) or (C <3 ) or ((R < 4) and (C < 4)):
            return "RICHARD"
        else:
            return "GABRIEL"

    elif X == 5:
        if (lol % 5 != 0) or (R < 3) or (C < 3) or ((R < 5) and (C < 5)):
             return "RICHARD"
        else:
            return "GABRIEL"
    elif X == 6:
        if (lol % 6 != 0) or (R < 3) or (C < 3) or ((R < 6) and (C < 6)):
            return "RICHARD"
        else:
            return "GABRIEL"
























