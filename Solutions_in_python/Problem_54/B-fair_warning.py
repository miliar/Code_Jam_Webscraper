import sys

def gcd(a, b):
    if a < b:
        a,b = b,a
    while b > 0:
        a, b = b, a % b
    return a

def test_gcd():
    for a, b, r in [ 
        (2,4,2), (10,15,5), (1,1,1), (1,8,1), (64,64,64), (48,32,16), (1000,700,100),
        (3,9,3), (17,34,17) ]:
        assert gcd(a,b) == r

def solve(items):
    if len(items) < 2:
        return 0
    g = abs( items[1] - items[0] )
    for idx in xrange(2,len(items)):
        g = gcd(g, abs(items[idx] - items[idx-1]))
    lack = items[0] % g
    if lack > 0:
        return g - lack
    else:
        return 0
    #return g - (items[0] % g)

if __name__ == "__main__":
    filename = sys.argv[1]
    input = open(filename)
    c = int(input.readline())
    for case_no in xrange(1, c+1):
        items = [ int(v) for v in input.readline().split() ]
        sol = solve(items[1:])
        print "Case #%d: %s" % (case_no, str(sol))



