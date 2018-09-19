output = []
T = int(input())
for i in range(T):
    X,R,C = input().split()
    X = int(X)
    R = int(R)
    C = int(C)
    flag = True

    if C < R:
        R ^= C
        C ^= R
        R ^= C

    if X == 1:
        flag = False
    elif X == 2:
        flag = (R&1) and (C&1)
    elif X == 3:
        if R == 1:
            flag = True
        elif R == 2:
            flag = (C != 3)
        elif R == 3:
            flag = False
        elif R == 4:
            flag = True
    elif X == 4:
        flag = not(R>=3 and C == 4)

    if flag:
        output.append("RICHARD")
    else:
        output.append("GABRIEL")

for i in range(T):
    print("Case #" + str(i+1) + ": " + output[i])
        
