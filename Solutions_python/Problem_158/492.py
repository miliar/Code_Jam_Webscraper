from sys import stdin

def each_case(X, R, C):
    if X == 1:
        return 'GABRIEL'
    if X == 2:
        if R % 2 and C % 2:
            return 'RICHARD'
        else:
            return 'GABRIEL'
    if X == 3:
        if R <= 1 or C <= 1 or (R % 3 and C % 3):
            return 'RICHARD'
        else:
            return 'GABRIEL'
    if X == 4:
        if R <= 2 or C <= 2 or (R*C) % 4:
            return 'RICHARD'
        else:
            return 'GABRIEL'
    assert False

T = int(stdin.readline())
for t in xrange(1,T+1):
    X, R, C = map(int, stdin.readline().split())
    print 'Case #{}: {}'.format(t, each_case(X, R, C))
