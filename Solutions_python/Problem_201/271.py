#!/usr/bin/env python3

"""
Bathroom Stalls

Author: Alex Dale - @SuperOxigen
"""

import fileinput

def f(n: int, k: int) -> (int, int):
    # if k > n:
        # print("ERROR f({}, {})".format(n, k))
    if n == k:
        return (0, 0)
    elif k == 1:
        if n % 2 == 0:
            return (n//2, n//2-1)
        else:
            return ((n-1)//2, (n-1)//2)
    elif n % 2 == 0:
        if k % 2 == 0:
            return f(n//2, k//2)
        else:
            return f(n//2-1, (k-1)//2)
    else:
        if k % 2 == 0:
            return f((n-1)//2, k//2)
        else:
            return f((n-1)//2, (k-1)//2)

def main():
    fin = fileinput.input()

    t = int(fin.readline().strip())

    for c in range(1, t+1):
        n, k = fin.readline().strip().split()
        n, k = int(n), int(k)

        ls, rs = f(n, k)
        print("Case #{}: {} {}".format(c, ls, rs))

if __name__ == "__main__":
    main()
