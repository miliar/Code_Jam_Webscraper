tc = int(input())
for c in range(1,tc + 1,1):
    X,R,C = list(map(int,input().split()))
    if R < C:
        R,C = C,R
    winner=""
    if (R*C) % X != 0:
        winner = "RICHARD"
    elif (X == 1) or (X == 2):
        winner = "GABRIEL"
    elif (X == 3):
        if (R == 3) and (C == 1):
            winner = "RICHARD"
        else:
            winner = "GABRIEL"
    elif (X == 4):
        if (R==4 and (C == 1 or C == 2)):
            winner = "RICHARD"
        elif (R == 2 and C == 2):
            winner = "RICHARD"
        else:
            winner = "GABRIEL"
    print("Case #{0}: {1}".format(c,winner))

            
