T = int(raw_input())

mat = [[[0,0,0,0,0],[0,1,0,1,0],[0,0,0,0,0],[0,1,0,1,0],[0,0,0,0,0]],
       [[0,0,0,0,0],[0,1,1,1,1],[0,1,1,0,1],[0,1,0,0,0],[0,1,1,0,1]],
       [[0,0,0,0,0],[0,1,1,1,1],[0,1,1,1,1],[0,1,1,1,0],[0,1,1,0,0]],
]

def calc(X, R, C):
    if X == 1:
        return False
    return mat[X-2][R][C]

for t in range(1, T+1):
    line = raw_input()
    X, R, C = [int(x) for x in line.split(' ')]
    if calc(X, R, C):
        print "Case #%d: RICHARD" % t
    else:
        print "Case #%d: GABRIEL" % t
