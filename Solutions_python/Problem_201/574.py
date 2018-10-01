from bisect import *
from collections import Counter

def ri():
    return int(raw_input().strip())

def ria(delim=" "):
    return [int(s) for s in raw_input().strip().split(delim)]

def bi(n):
    a = n / 2
    b = n - a
    return (max(a, b), min(a, b))

def main():
    t = ri()
    for c in xrange(1, t + 1):
        n, k  = ria()
        cter = Counter([n])

        while k > 1:
            maxsize = max(cter)
            todiv = min(k - 1, cter[maxsize])
            k -= todiv
            cter[maxsize] -= todiv
            if cter[maxsize] == 0:
                del cter[maxsize]
            mx, mn        = bi(maxsize)
            cter[mx - 1] += todiv
            cter[mn]     += todiv
        
        maxsize = max(cter)
        mx, mn = bi(maxsize - 1)
        print "Case #{}: {} {}".format(c, mx, mn)

main()