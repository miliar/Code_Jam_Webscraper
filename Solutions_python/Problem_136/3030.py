
from sys import stdin

t = int(stdin.readline())

for num in range(0, t):
    row = stdin.readline().strip()
    values = row.split(' ')
    c = float(values[0])
    f = float(values[1])
    x = float(values[2])
    time = 0.0
    cps = 2.0
    toContinue = True
    while (toContinue):
        timeToFinish = x / cps
        timeToNextFarm = c / cps
        timeToFinishWithNextFarm = x / (cps + f)
        if (timeToFinish < timeToNextFarm + timeToFinishWithNextFarm):
            time = time + timeToFinish
            toContinue = False
        else:
            time = time + timeToNextFarm
            cps = cps + f
    print("Case #%d: %.7f" % (num + 1, time))
