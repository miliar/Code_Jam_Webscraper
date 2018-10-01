import sys, math

    
num_cases = int(sys.stdin.readline())


def get_tests(l, p, c):
    if l * c >= p:
        return 0

    pivot = math.ceil(l * (float(p)/l)**0.5)

    return 1 + max(get_tests(l, pivot, c), get_tests(pivot, p, c))


for j in xrange(num_cases):
    l, p, c = [int(e) for e in sys.stdin.readline().split()]

    print "Case #%s: %s" % (j+1, get_tests(l, p, c))
    j += 1
