import fileinput

def checkVals(N,K):
    mask = (1<<N)-1
    return (K & mask) == mask

def main():
    it = fileinput.input()
    caseCount = int(it.next())
    for (caseNum,l) in enumerate(it):
        (N,K) = [int(x) for x in l.split()]
        if checkVals(N,K):
            print "Case #%d: ON" % (caseNum + 1)
        else:
            print "Case #%d: OFF" % (caseNum + 1)

if __name__ == "__main__":
    main()
