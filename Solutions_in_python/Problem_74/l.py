fp = open('A-large-attempt0.in')
T = int(fp.readline())

for t in range(T):
    a = fp.readline().strip().split()
    q = a[1:]
    D =  {'O':1, 'B':1}
    LT = {'O':0, 'B':0}
    TA = []
    LR = 'X'
    TIME = 0
    while len(q)>0:
        R = q.pop(0)
        P = int(q.pop(0))
        time = max((abs(D[R]-P)-(LR!=R)*(TIME-LT[R])),0)+1
        TIME += time
        LT[R] = TIME
        D[R] = P
        LR = R
    print "Case #%d:"%(t+1),TIME