import math

def getDistribution(n, k):
    lbase2 = math.log(k, 2)
    lbint = int(lbase2)
    lb = math.pow(2, lbint)
    lb1 = math.pow(2, lbint + 1)
    l = math.ceil( (n-k+1) / ((lb1 - lb )))
    # print l
    return int(l)
    fint = int(n / lb)
    fint = fint if lbase2 == lbint else fint - 1
    return fint


def getStalls(n, k):
    baseval = getDistribution(n, k)
    if baseval == 0:
        return (0, 0)
    # print baseval ;
    baseval = baseval - 1;

    ls = int(baseval / 2);
    rs = baseval - ls
    if ls > rs:
        return ls, rs
    else:
        return rs, ls

t = int(raw_input())
for i in range(t):
    nandk = map(int, raw_input().split())
    remstalls = getStalls(nandk[0], nandk[1])
    print "Case #{}: {} {}".format(i+1, remstalls[0], remstalls[1])
