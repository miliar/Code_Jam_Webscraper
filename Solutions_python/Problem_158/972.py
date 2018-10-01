import fileinput
input = fileinput.input()
get = lambda t: list(t(i) for i in input.readline().strip().split())

def solve_case(casenum):
    X, R, C = get(int)
    R, C = sorted((R, C))
    size = R, C
    if X == 1:
            return True
    elif X == 2:
        if R % 2 == 0 or C % 2 == 0:
            return True
    elif X == 3:
        if size == (2, 3) or size == (3, 3) or size == (3, 4):
            return True
    elif X == 4:
        if size == (3, 4) or size == (4, 4):
            return True
    return False


T = get(int)[0]
for c in range(T):
    if solve_case(c):
        print('Case #%s: %s' % (c+1, 'GABRIEL'))
    else:
        print('Case #%s: %s' % (c+1, 'RICHARD'))




