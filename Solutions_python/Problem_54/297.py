import fractions
import sys

N = int(sys.stdin.readline())
case = 0
for line in sys.stdin:
    case += 1

    # read input
    parts = line.split(' ')
    assert int(parts[0]) == (len(parts) - 1)
    inputs = [ int(p) for p in parts[1:] ]

    # get the differences between adjacent inputs
    diffs = [ ]
    for i in xrange(1, len(inputs)):
      diffs.append(abs(inputs[i] - inputs[i-1]))

    # compute the result
    gcd = diffs[0]
    for d in diffs:
      gcd = fractions.gcd(gcd, d)

    res = (gcd - (inputs[0] % gcd)) % gcd
    print 'Case #%d: %d' % (case, res)



