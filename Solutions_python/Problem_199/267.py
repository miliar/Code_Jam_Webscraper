#!/usr/bin/env python3

"""
Oversized Pancake Flipper

Author: Alex Dale - @SuperOxigen
"""

import fileinput


def convertString(string: str) -> (list, int):
    bits = [True] * len(string)

    m = 0

    for i in range(len(string)):
        if string[i] == "-":
            m += 1
            bits[i] = False

    return bits, m

def main():
    fin = fileinput.input()

    t = int(fin.readline().strip())

    for c in range(1, t+1):
        string, k = fin.readline().strip().split()
        k = int(k)
        s = len(string)

        bits, m = convertString(string)

        n = 0
        for i in range(s-k+1):
            if not bits[i]:
                n += 1
                for j in range(k):
                    bits[i+j] = not bits[i+j]

        if not all(bits):
            print("Case #{}: IMPOSSIBLE".format(c))
        else:
            print("Case #{}: {}".format(c, n))

if __name__ == "__main__":
    main()
