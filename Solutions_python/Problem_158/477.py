import math
T=int(input())
for t in range(0,T):
    L=input().split(" ")
    X=int(L[0])
    R=int(L[1])
    C=int(L[2])
    X2=int(math.sqrt(float(X)))
    X3=int((X+1)/2)
    X4=int(X/2)
    if X > R*C:
        W="RICHARD"
    elif X2 > R:
        W="RICHARD"
    elif X2 > C:
        W="RICHARD"
    elif X3 > R:
        W="RICHARD"
    elif X3 > C:
        W="RICHARD"
    elif (X > R) and (X > C):
        W="RICHARD"
    elif X < 2:
        W="GABRIEL"
    elif ((R*C) % X) != 0:
        W="RICHARD"
    elif X < 4:
        W="GABRIEL"
    elif (R <= X4) or (C <= X4):
        W="RICHARD"
    else:
        W="GABRIEL"
    print("Case #%d: %s"%(t+1,W))
                
