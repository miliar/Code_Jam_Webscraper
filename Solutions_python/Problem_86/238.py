import sys, gmpy2


def getharmony(freqdata):
    numperfs, mylow, myhigh = freqdata[0]
    perfs = freqdata[1]

    for i in range(mylow, myhigh+1):
        found = True
        for n in perfs:
            if n % i == 0 or i % n == 0:
                pass
            else:
                found = False
                break

        # if we got here, OK
        if found: return i

    return "NO"

def processtestcases():
    numtestcases = int(sys.stdin.readline().rstrip())
    testcases = []

    for i in range(numtestcases):
        metadata = [int(a) for a in sys.stdin.readline().rstrip().split(' ')]
        freqs = [int(a) for a in sys.stdin.readline().rstrip().split(' ')]
        #print str([metadata,freqs])
        testcases.append([metadata,freqs])

    return testcases


if __name__ == "__main__":
    testcases = processtestcases()
    #print str(testcases)
    i = 1
    for testcase in testcases:
        print "Case #"+str(i)+": "+str(getharmony(testcase))
        i += 1





