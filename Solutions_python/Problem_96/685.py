if __name__ == '__main__':
    import sys
    fname = sys.argv[1]
    inFile = open(fname, 'r')
    numCases = int(inFile.readline())
    for case in xrange(numCases):
        # Get the number range
        nums = map(int, inFile.readline().split())
        n,s,p = nums[:3]
        T = nums[3:]
        sure = 3 * p - 2
        surprise = 3 * p - 4
        print 'Case #%d: %s' % (case + 1,
                len([t for t in T if t >= sure]) + min(s,
                    len([t for t in T if surprise <= t < sure and t > 0])))
    inFile.close()
