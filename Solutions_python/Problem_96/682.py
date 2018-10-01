import sys
from B import max_googlers as mg

_in = sys.stdin

if __name__ == '__main__':
    n = int(_in.readline())
    for i in range(n):
        _l = list(map(int, _in.readline().split()))
        print("Case #%d: %d" % (i+1, mg(_l[0],_l[1],_l[2],_l[3:])))
