
import sys

def negate(x):
    return [-elt for elt in x]

def absval(x):
    return [abs(elt) for elt in x]

def sign(x):
    return x[0] or x[1] or x[2] or x[3]

def binary_product(x, y):
    if x[0] == 1:
        return y
    if y[0] == 1:
        return x
    if x[0] == -1:
        return negate(y)
    if y[0] == -1:
        return negate(x)
    if x == y:
        return [-1, 0, 0, 0]
    if x == negate(y):
        return [1, 0, 0, 0]

    sgn = sign(x) * sign(y)
    x, y = absval(x), absval(y)

    if x[1] and y[2]:
        return [0, 0, 0, sgn]
    if x[1] and y[3]:
        return [0, 0, -sgn, 0]
    if x[2] and y[1]:
        return [0, 0, 0, -sgn]
    if x[2] and y[3]:
        return [0, sgn, 0, 0]
    if x[3] and y[1]:
        return [0, 0, sgn, 0]
    if x[3] and y[2]:
        return [0, -sgn, 0, 0]


I = [0, 1, 0, 0]
J = [0, 0, 1, 0]
K = [0, 0, 0, 1]
ValMap = {'i': I, 'j': J, 'k': K}

def partial_values(s):
    L = [None] * len(s)
    V = [1, 0, 0, 0]
    for i, ch in enumerate(s):
        factor = ValMap[ch]
        V = binary_product(V, factor)
        L[i] = V
    return L

def test_string(s):
    vals = partial_values(s)
    min_left = None
    max_right = None

    if vals[-1] != [-1, 0, 0, 0]:
        return False

    for a in xrange(len(s)):
        if vals[a] == I:
            min_left = a
            break

    for b in xrange(len(s) - 1, -1, -1):
        if vals[b] == K:
            max_right = b
            break

    return min_left is not None  and \
           max_right is not None and \
           min_left < max_right


num_cases = int(sys.stdin.readline())
for casenum in xrange(num_cases):
    _, rep = sys.stdin.readline().strip().split(" ")
    rep = int(rep)
    s = sys.stdin.readline().strip()

    result = test_string(s * rep)
    print "Case #%d: %s" % (casenum+1, 'YES' if result else 'NO')

