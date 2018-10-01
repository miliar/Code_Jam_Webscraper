import math
from functools import lru_cache

@lru_cache(maxsize=100000)
def ispalindrome(n):
    oldn = n
    rev = 0
    while n > 0:
        rev = 10 * rev + n % 10
        n = n // 10
    return rev == oldn

@lru_cache(maxsize=100000)
def fairsquare(i, j):
    sqrti = int(math.sqrt(i))
    sqrtj = int(math.sqrt(j))
    res = 0
    for a in range(sqrti, sqrtj+1):
        if ispalindrome(a):
            sqra = a * a
            if ispalindrome(sqra):
                if sqra >= i and sqra <= j:
                    res += 1
    return res

def printres(i, res):
    print("Case #%d: %d" % (i, res))

def main():
    import sys
    for i, line in enumerate(sys.stdin):
        if i == 0:
            continue
        args = [int(i) for i in line.split()]
        printres(i, fairsquare(*args))

if __name__ == "__main__":
    main()
