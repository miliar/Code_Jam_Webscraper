import sys, re

def makemagic(data):
    # prepare input
    dstack = []

    transformdict = data[0]
    clearsets = data[1]

    for curitem in data[2]:

        # add to wip data
        dstack.append(curitem)

        # round 1: transforms
        if len(dstack) < 2:
            pass
        else:
            endstring = ''.join(sorted(dstack[-2:]))
            if endstring in transformdict:
                dstack.pop()
                dstack.pop()
                dstack.append(transformdict[endstring])

            dset = set(dstack)
            for clearset in clearsets:
                if clearset <= dset:
                    dstack = []
                    break

    return dstack        
        


def processtestcases():
    numtestcases = int(sys.stdin.readline().rstrip())
    testcases = []
    
    # read in instructions for each test case
    for i in range(numtestcases):
        mode1items = {}
        mode2items = []
        mode3items = []

        inputs = sys.stdin.readline().rstrip().split(' ')
        j = 0
        num_itemstoread = 0

        # mode 1: C
        num_itemstoread = int(inputs[j])
        for k in range(num_itemstoread):
            clist = inputs[j+k+1]
            cin = ''.join(sorted(list(clist[0:2])))
            mode1items[cin] = clist[2]
        j += num_itemstoread + 1

        # mode 2: D
        num_itemstoread = int(inputs[j])
        for k in range(num_itemstoread):
            mode2items.append(set(inputs[j+k+1]))
        j += num_itemstoread + 1

        # mode 3: N
        mode3items = list(inputs[j+1])

        # add together
        testcases.append([mode1items, mode2items, mode3items])

    return testcases


if __name__ == "__main__":
    testcases = processtestcases()
    #print str(testcases)
    i = 1
    for testcase in testcases:
        outset = makemagic(testcase)
        print "Case #"+str(i)+": "+re.sub("'","",str(outset))
        i += 1





