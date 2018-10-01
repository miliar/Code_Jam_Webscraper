import sys

def checkline(l):
    for a in l:
        if a.count("X") + a.count("T") == 4:
            return "X"
        if a.count("O") + a.count("T") == 4:
            return "O"
    return None

def checkrow(l):
    for i in xrange(4):
        a = l[0][i] + l[1][i] + l[2][i] + l[3][i]
        if a.count("X") + a.count("T") == 4:
            return "X"
        if a.count("O") + a.count("T") == 4:
            return "O"
    return None


def checkdiags(l):
    A = l[0][0] + l[1][1] + l[2][2] + l[3][3]
    AA = l[3][0] + l[2][1] + l[1][2] + l[0][3]
    for a in [A,AA]:
        if a.count("X") + a.count("T") == 4:
            return "X"
        if a.count("O") + a.count("T") == 4:
            return "O"
    return None

def finddot(l):
    for a in l:
        if a.find(".") >= 0:
            return True
    return False




for i in xrange(1, 1+int(sys.stdin.readline())):
    l = []
    for j in xrange(4):
        l.append(sys.stdin.readline().replace("\n", ""))

    s = ""
    t = checkrow(l)
    if not t:
        t = checkline(l)
    if not t:
        t = checkdiags(l)
    if t:
        s = "%s won" % t
    else:
        if finddot(l):
            s = "Game has not completed"
        else:
            s = "Draw"

    print "Case #%d: %s" % (i, s)
    sys.stdin.readline().replace("\n", "") # The empty line
