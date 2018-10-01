def readval(typ=int):
    return typ( raw_input() )

def readvals(typ=int):
    return map( typ, raw_input().split() )

def testcase(cas=-1):
    Ac, Aj = readvals() 
    CD = [readvals() for _ in xrange(Ac)]
    JK = [readvals() for _ in xrange(Aj)]
    if Ac+Aj==1: res = 2
    elif Ac==1 and Aj==1: res = 2
    elif Ac==2:
        C, D = zip(*CD)
        len1 = (D[1] + 1440 - C[0]) % 1440
        len2 = (D[0] + 1440 - C[1]) % 1440 
        if len1 <=720 or len2 <=720: res = 2
        else: res = 4
    elif Aj==2:
        J, K = zip(*JK)
        len1 = (K[1] + 1440 - J[0]) % 1440
        len2 = (K[0] + 1440 - J[1]) % 1440 
        if len1 <=720 or len2 <=720: res = 2
        else: res = 4
    print 'Case #%d: %d' % ( cas, res )

if __name__=='__main__':
    T = readval()
    for i in xrange(T):
        testcase(i+1)
