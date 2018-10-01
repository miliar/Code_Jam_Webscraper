#!/usr/bin/python

KEY = 'welcome to code jam'
STR = ''
HASH = dict()

def solve(s, k):
    if HASH.has_key((s, k)):
        return HASH[(s, k)]

    R = 0
    if (KEY[k:] == '') or (STR[s:] == KEY[k:]):
        R = 1
    else:
        if (STR[s:] != ''):
            i = 0
            while (s+i < len(STR)) and (STR[s+i] == KEY[k]):
                i = i+1
            if i > 0:
                R = i*solve(s+i, k+1)
            R = R + solve(s+i+1, k)
    HASH[(s, k)] = R
    return R

if __name__ == '__main__':
    import sys
    inp = open(sys.argv[1], "r")
    T = int(inp.readline())
    for k in range(T):
        STR = inp.readline()
        HASH = dict()
        N = str(solve(0, 0))
        if len(N) >= 4:
            N = N[-4:]
        else:
            N = '%s%s' % ('0'*(4-len(N)), N)
        print 'Case #%s: %s' % ((k+1), N)
