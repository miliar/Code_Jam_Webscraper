import math

t = int(raw_input())

def main():
    for _ in xrange(t):
        d = int(raw_input())
        p = [int(i) for i in raw_input().split(" ")]

        #print d
        #print p

        pmax = max(p)
        pmin = min(p)
        result = pmax

        pmax2 = int(math.ceil(pmax / 2.0))
        for x in xrange(pmax2, pmax):
            pppmax = sum((1 for i in p if i > x))
            #print pmax, pppmax + x, pppmax, x
            result = min(result, pppmax + x)

        pmax3 = int(math.ceil(pmax / 3.0))
        for x in xrange(pmax3, pmax):
            ppppmax = sum((2 for i in p if i > x))

            a = [i for i in p if i <= x]
            if not a:
                result = min(result, ppppmax + pmax3)
                continue

            pmax2 = int(math.ceil(max(a) / 2.0))
            for y in xrange(pmax2, pmax):
                pppmax = sum((1 for i in p if y < i and i <= x))
                #print pmax, ppppmax + pppmax + y, ppppmax, pppmax, y
                result = min(result, ppppmax + pppmax + max(pmax3, y))

        print "Case #{}: {}".format(_ + 1, result)

main()
