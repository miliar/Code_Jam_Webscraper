import sys

def calculate(c, f, x):
    result = []
    nf = 0
    result.append(x / 2)
    tmin = result[-1]
    while result[-1] <= tmin:
        nf += 1
        ff = 0
        totaltime = 0
        rate = 2
        while ff < nf:
            totaltime += c / rate
            ff += 1
            rate += f
        totaltime += x / rate
        result.append(totaltime)
        tmin = min(tmin, totaltime)
    return result[-2]

lines = sys.stdin.readlines()
t = int(lines[0])
for i in range(1, t + 1):
    tmp = map(float, lines[i].split())
    c = tmp[0]
    f = tmp[1]
    x = tmp[2]
    print "Case #%d: %.7f"%(i,calculate(c, f, x))