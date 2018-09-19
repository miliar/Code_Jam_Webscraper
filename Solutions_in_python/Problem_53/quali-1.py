# python 2.5

import sys
pof2s = [pow(2, i) for i in range(31)]
stdinreadline = sys.stdin.readline

def status(data):
    n, k = data
    if (k+1)% pof2s[n] == 0:
        return "ON"
    else:
        return "OFF"

T = int(stdinreadline())
for i in range(1, T+1):
    print "Case #%d: %s" % (i, status(map(int, stdinreadline().split())))
