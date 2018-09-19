f = open('D-small.in')
g = open('small.out', 'w')

T = int(f.readline()[:-1])

def solve(X, R, C) :
    if X == 1 : return 'GABRIEL'
    if R*C % X != 0 : return 'RICHARD'
    if X == 2 : return 'GABRIEL'
    m, M = min(R, C), max(R, C)
    s, B = X - X/2, X/2 + 1
    if B > M or s > m : return 'RICHARD'
    if B < M and s < m : return 'GABRIEL'
    if X == 3 : return 'GABRIEL'
    return 'RICHARD'

for case in range(T) :
    X, R, C = map(int, f.readline()[:-1].split())
    res = solve(X, R, C)
    output = 'Case #' + str(case+1) + ': ' + str(res)
    print output
    g.write(output + '\n')

f.close()
g.close()
