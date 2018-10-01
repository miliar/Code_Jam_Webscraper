import os
import sys


if __name__ == "__main__":
    with open('A-large.in', 'r') as f:
        n = int(f.readline())
        for i in range(n):
            d, m = f.readline().strip().split(' ')
            d = float(d)
            maxT = 0.0
            for j in range(int(m)):
                k, s = f.readline().strip().split(' ')
                k = float(k)
                s = float(s)
                if (d - k) / s > maxT:
                    maxT = (d -k) / s
            print("Case #%d: %.6lf" % (i+1, d / maxT))
