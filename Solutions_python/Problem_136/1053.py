def calcP(C, F):
    p = 0
    nn = 0
    while True:
        yield (p,nn)
        p = p + (C/(2.0 + F*nn)) 
        nn+=1

N = int(raw_input())
for n in range(N):
    [C, F, X] = [float(v) for v in raw_input().split()]
    minc = 100000000000000000000000 ## LOL whatever 
    for (P, nn) in calcP(C, F):
        c = X/(2.0 + F*nn) + P
        if c > minc:
            break
        minc = c
    print("Case #%d: %.7f" % (n+1, minc))
