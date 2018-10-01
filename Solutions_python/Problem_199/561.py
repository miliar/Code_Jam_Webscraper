def ri():
    return int(raw_input().strip())

def rsa(delim=" "):
    return raw_input().strip().split(delim)


def flip(cakes, pos, size):
    sub = cakes[pos : pos + size]
    cakes[pos : pos + size] = map(lambda cake: not cake, sub)

def main():
    t = ri()
    for case in xrange(t):
        cakestr, sizestr = rsa()
        size  = int(sizestr)
        cakes = [c == '+' for c in cakestr]

        flips = 0
        for i in xrange(len(cakes) - size + 1):
            if not cakes[i]:
                flip(cakes, i, size)
                flips += 1

        if all(cakes):
            print "Case #{}: {}".format(case + 1, flips)
        else:
            print "Case #{}: IMPOSSIBLE".format(case + 1)


main()