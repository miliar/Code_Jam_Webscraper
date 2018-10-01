import math

def memoize(f):
    cache = {}
    def g(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return g

lines = []
with open('C-large.in', 'r') as f:
    lines = f.read().split("\n")

cases = int(lines.pop(0))

@memoize
def f(s1, s2, idx, l):
    # global l
    if s2 == "":
        return 1
    i = idx
    while i < len(l):
        c = l[i]
        if c == s2[0]:
            return f(s1 + c, s2[1:], i + 1, l) + f(s1, s2, i + 1, l) % 10000
        i += 1
    return 0

def solve(l):
    return f("", "welcome to code jam", 0, l)

l = ""
for c in range(cases):
    l = lines.pop(0)
    print "Case #%d: %s" % (c + 1, ("0000" + str(solve(l)))[-4:])
