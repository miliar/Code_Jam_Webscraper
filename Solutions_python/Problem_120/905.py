import sys
import fileinput
import math
from decimal import getcontext, Decimal

fin = fileinput.input()
fout = sys.stdout

def solve(r, t):
    getcontext().prec = 1000
    result = math.floor((Decimal(-2 * r + 1) + (Decimal((2 * r - 1)**2 + 8 * t)).sqrt()) / Decimal(4))
    assert result > 0
    return int(result)

def main():
    T = int(fin.readline())
    
    for case_idx in xrange(T):
        r, t = tuple(map(int, fin.readline().split()))
        
        result = solve(r, t)
        
        fout.write("Case #{0}: {1}\n".format(case_idx + 1, result))

if __name__ == "__main__":
    main()
