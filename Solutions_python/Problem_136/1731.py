def main():
    numOfIter = int(raw_input())
    for i in xrange(numOfIter):
        (farmCost, farmCookies, target) = parseData()
        minResult = 1000000000
        lastMinResult = minResult
        farms = 0
        while (lastMinResult >= minResult):
            lastMinResult = minResult
            minResult = 0
            for farm in xrange(farms):
                minResult += farmCost / float(farmCookies * farm + 2)
            minResult += target / float(farms * farmCookies + 2)
            farms += 1
        print "Case #%d: %.7f" % (i + 1, lastMinResult)

def parseData():
    return [float(x) for x in raw_input().split(" ")]

if __name__ == "__main__":
    main()
