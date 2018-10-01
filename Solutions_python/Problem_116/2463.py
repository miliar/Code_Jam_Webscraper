import sys

def diag(p):
    return [p[i][i] for i in xrange(len(p))]

def check_row(row):
    return set(row).issubset(set("XT")), set(row).issubset(set("OT"))

def solve(p):
    X, O = False,False
    Full = not any("." in row for row in p)
    rows = p + zip(*p) + [diag(p)] + \
            [diag([tuple(reversed(row)) for row in p])]
    for row in rows:
        Xc, Oc = check_row(row)
        X,O = (X or Xc, O or Oc)

    if X and O:
        raise Exception
    elif X:
        return "X won"
    elif O:
        return "O won"
    elif Full:
        return "Draw"
    else:
        return "Game has not completed"

sys.stdin.next()
i = 1
while True:
    try:
        problem = [sys.stdin.next().strip() for _ in xrange(4)]
        print "Case #%d:" % i, solve(problem)
        i += 1
        sys.stdin.next()
    except StopIteration:
        break
