import math

def isTidy(n):
    x = [int(d) for d in str(n)]
    y = all(x[i] <= x[i+1] for i in xrange(len(x)-1))
    return y


t = int(raw_input())
for i in range(1, t + 1):
    inp = int(raw_input())
    res = 0;
    while(inp != 0):
        if(isTidy(inp)):
            res = inp
            break
        else:
            inp = inp - 1
    print("Case #{}: {}".format(i, res))