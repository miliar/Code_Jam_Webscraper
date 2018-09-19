#!/usr/bin/env python

import sys

def input_int():
    return int(sys.stdin.readline().strip())
def input_list():
    raw = sys.stdin.readline().strip()
    return map(int, raw.split())

def solve1(N, K):
    '''
    @param N: Number of snapper devices.
    @param K: Number of times to snap fingers.
    '''
    OFF = 0
    ON = 1
    snappers = [OFF]*N
    for k in xrange(K):
        S = snappers[:]
        power = True
        for i in xrange(N):
            if power:
                S[i] = int(not snappers[i])
                if snappers[i] == 0:
                    power = False
            else:
                break
        #print k+1, S
        snappers = S
    if snappers == [ON]*N:
        return 'ON'
    return 'OFF'

def solve2(N, K):
    # Faster...
    if (K + 1) % (2**N) == 0:
        return 'ON'
    return 'OFF'

if __name__ == '__main__':
    T = input_int()
    for t in xrange(T):
        N, K = input_list()
        solution = solve2(N, K)
        print 'Case #%d: %s' % (t+1,solution)

