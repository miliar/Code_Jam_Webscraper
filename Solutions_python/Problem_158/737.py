with open("D-small-attempt3.in","r") as f:
    numOfCase = int(f.readline())
    print(numOfCase)
    for i in range(numOfCase):
        ans = "RICHARD"
        lines = f.readline().split()
        X = int(lines[0])
        R = int(lines[1])
        C = int(lines[2])
        if (X < 4):
            if (X == 3):
                if ((R*C)%X == 0 and (R*C >= 2*X)):
                    ans = "GABRIEL"
            elif ((R*C)%X == 0):
                ans = "GABRIEL"
        else:
            if (R > 2 and C > 2):
                if ((R*C)%X == 0):
                    ans = "GABRIEL"       
        print("Case #%d: %s" % (i+1,ans))
f.closed





