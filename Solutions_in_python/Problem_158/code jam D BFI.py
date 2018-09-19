import math
testCases = int(input())


for i in range(testCases):
    x, r, c = input().split(" ")
    x = int(x)
    r = int(r)
    c = int(c)
    if r > c:
        r, c = c, r
    if (r*c)%x != 0:
        print("Case #{}: RICHARD".format(i+1))
    elif x == 1:
        print("Case #{}: GABRIEL".format(i+1))
    elif x == 2:
        if c == 1:
            print("Case #{}: RICHARD".format(i+1))
        else:
            print("Case #{}: GABRIEL".format(i+1))
    elif x == 3:
        if c < 3:
            print("Case #{}: RICHARD".format(i+1))
        elif r == 1:
            print("Case #{}: RICHARD".format(i+1))
        else:
            print("Case #{}: GABRIEL".format(i+1))
    elif x == 4:
        if c < 4:
            print("Case #{}: RICHARD".format(i+1))
        elif r < 3:
            print("Case #{}: RICHARD".format(i+1))
        else:
            print("Case #{}: GABRIEL".format(i+1))
        
    
