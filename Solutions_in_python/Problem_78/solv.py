import sys, unittest

def canCalcPersentage(todayN, percent):
    if percent == 0:
        return True
    return percent * todayN % 100 == 0

def canCalcPersentages(todayN, percent):
    for n in range(1, todayN+1):
        if canCalcPersentage(n, percent):
            return True
    return False

def isPossible(N, Pd, Pg):
    if Pg == 100 and Pd != 100:
        return False
    if Pg == 0 and Pd != 0:
        return False
    return True

def isPossibleString(N, Pd, Pg):
    if isPossible(N,Pd,Pg) and canCalcPersentages(N, Pd):
        return 'Possible'
    return 'Broken'

def solvProblem(lines):
    result = []
    for line in lines:
        (N, Pd, Pg) = [int(n) for n in line.split()]
        result.append(isPossibleString(N, Pd, Pg))
    return result

class Test(unittest.TestCase):
    def testCanCalcPersentage(self):
        self.assertTrue( canCalcPersentage(5, 80) )
        self.assertFalse( canCalcPersentage( 6, 80) )

    def testCanCalcPersentages(self):
        self.assertTrue( canCalcPersentages(7, 80) )
        self.assertFalse( canCalcPersentages(6, 42) )
        self.assertTrue( canCalcPersentages(4, 25) )

if __name__ == '__main__':
    if len(sys.argv) > 1:
        lines = [line.rstrip() for line in open(sys.argv[1])]
        count = 1
        result = solvProblem(lines[1:])
        for r in result:
            print 'Case #%d: %s' % (count, r)
            count += 1
    else:
        unittest.main()

