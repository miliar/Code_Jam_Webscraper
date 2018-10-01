def ceckPal(p):
    p=str(p)
    rit = True
    for k in range(len(p)/2):
        if p[k] != p[-k-1]:
            rit = False
            break
    return rit

def getPal(input):
    
    #Function used to obtain PerfectPal with input = 7
    
    from numpy import base_repr
    print 'PerfectPal = ['
    print '1,'
    print '4,' 
    print '9,' 
    for k in range(2, input+1):
        for j in range(3**(k/2-1),3**(k/2)):
            if k % 2 == 1:
                for m in range(3): 
                    a = int(base_repr(j, base=3)+str(m)+base_repr(j, base=3)[::-1])
                    if ceckPal(a**2): print str(a**2)+','
            if k % 2 == 0:
                a = int(base_repr(j, base=3)+base_repr(j, base=3)[::-1])
                if ceckPal(a**2): print str(a**2)+','
    print ']'

PerfectPal = [
1,
4,
9,
121,
484,
10201,
12321,
14641,
40804,
44944,
1002001,
1234321,
4008004,
100020001,
102030201,
104060401,
121242121,
123454321,
125686521,
400080004,
404090404,
10000200001,
10221412201,
12102420121,
12345654321,
40000800004,
1000002000001,
1002003002001,
1004006004001,
1020304030201,
1022325232201,
1024348434201,
1210024200121,
1212225222121,
1214428244121,
1232346432321,
1234567654321,
4000008000004,
4004009004004,
]
    
def setup(infile):
    #C = {}
    return locals()

def reader(testcase, infile, **ignore):
    return locals()

def solver(infile, testcase, N=None, P=None, I=None, T=None, S=None, C=None, **ignore):
    k1, k2 = map(lambda k: int(k),infile.next().split())
    res = 0
    for k in PerfectPal:
        if k1<=k<=k2: res += 1
    return 'Case #%s: %s\n' % (testcase, res)

if __name__ == '__main__':
    import sys
    T = int(sys.stdin.next())
    common = setup(sys.stdin)
    for t in xrange(1, T+1):
        sys.stdout.write(solver(**reader(t, **common)))
