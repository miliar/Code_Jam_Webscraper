lines = open("a.in").readlines()
f = open('out.txt', 'w')

for i in xrange(0, int(lines.pop(0))):
    totalTime = 0.0
    currentCookies = 2
    costOfFarm, incCookies, goal = map(lambda l: float(l), lines.pop(0).split())
    timeWithoutFarm = goal/currentCookies
    timeWithFarm = costOfFarm/currentCookies + goal/(currentCookies + incCookies)
    while timeWithFarm < timeWithoutFarm:
        totalTime += costOfFarm/currentCookies
        currentCookies += incCookies
        timeWithoutFarm = goal/currentCookies
        timeWithFarm = costOfFarm/currentCookies + goal/(currentCookies + incCookies)
    totalTime += timeWithoutFarm
    f.write("Case #{0}: {1}\n".format(i+1, totalTime))




