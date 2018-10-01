input = open("Input.txt")
output = open("Output.txt", 'w')

C = int(input.readline())

def gcd(a, b):
    if b == 0: return a
    else: return gcd(b, a % b)

def f(ll):
    d = abs(ll[0] - ll[1])
    for i in xrange(2, len(ll)):
        d = gcd(d, abs(ll[i] - ll[i - 1]))
    m = ll[0] % d
    if m == 0: return 0
    return d - m

test = 1
for line in input:
    ar = str.split(line)
    k = []
    for i in xrange(int(ar[0])):
        k.append(int(ar[i + 1]))
    print >> output, "Case #{0}: {1}".format(test, f(k))
    test += 1
