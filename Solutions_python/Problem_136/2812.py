#!/usr/bin/python
from decimal import Decimal

myFile = open("inputCookies.txt")
nCases = (int)(myFile.next())

for i in xrange(nCases) :
    curCase = i+1

    values = (myFile.next()).split()
    C = Decimal((float)(values[0]))
    F = Decimal((float)(values[1]))
    X = Decimal((float)(values[2]))

    rate = Decimal(2.0)
    cookies = Decimal(0.0)
    totalTime = Decimal(0.0)

    while cookies < X :
        ttFinished = (X-cookies)/rate
        ttNextFarm = (C-cookies)/rate
        ttFinishedFarm = ttNextFarm+(X)/(rate+F)

        if ttFinished > ttFinishedFarm :
            totalTime = totalTime + ttNextFarm
            rate = rate + F
        else :
            cookies = X
            totalTime = totalTime + ttFinished

    print "Case #%d: %.7f" % (curCase,totalTime)



