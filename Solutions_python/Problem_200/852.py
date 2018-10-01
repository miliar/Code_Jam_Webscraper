import sys

T = int(sys.stdin.readline())

for t in xrange(T):
    origN = sys.stdin.readline().strip()
    N = [int(x) for x in origN];

    good = True
    prev = 0
    index = 0
    for i in xrange(len(N)):
        if N[i] > prev:
            index = i
        elif N[i] < prev:
            good = False
            break
        prev = N[i]

    result = origN
    if good:
        result = origN
    else:
        result = ''
        for i in xrange(index):
            result += str(N[i])
        if index > 0 or N[index] - 1 > 0:
            result += str(N[index] - 1)
        result += (len(N) - index - 1) * '9'
    print("Case #%d: %s" % (t + 1, result))
