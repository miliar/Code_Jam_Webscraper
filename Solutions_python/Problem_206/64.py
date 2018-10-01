#!/usr/bin/python3
__author__ = 'Tianren Liu'

import sys
import numpy as np

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for _t in range(1,T+1):
        D,N = map(int, sys.stdin.readline().split())

        t = max((D-K)/S for K,S in (map(int, sys.stdin.readline().split()) for _ in range(N)))

        print("Case #{}: {}".format(_t, D/t))
