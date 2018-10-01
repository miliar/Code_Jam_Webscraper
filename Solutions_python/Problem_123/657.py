from __future__ import print_function
"""
"""
try:
    range = xrange
    input = raw_input
except NameError: # Python 3
    pass

try:
    from future_builtins import *
except ImportError: # Python 3
    pass

def f(A, motes, n=0):
    k = len(motes)
    if k == 0: # no more motes to eat
        return n
    elif A == 1:
        # can't eat any mote (all sizes are >=1)
        # no point to add mote even with size 1 (can't eat it)
        return n + len(motes) # remove all motes
    else: # len(motes) > 0 and A > 1
        # eat all motes that we can
        for i, m in enumerate(motes):
            if m >= A:
                break
            else: # eat
                A += m
        else: # all eaten
            return n

        # add mote or remove it
        return min(f(A + A-1, motes[i:], n+1), f(A, motes[i:-1], n+1))

def main():
    for i in range(1, int(input()) + 1):
        A, N = map(int, input().split())
        motes = [int(s) for s in input().split()]
        assert len(motes) == N
        print("Case #%d: %d" %  (i, f(A, sorted(motes))))

main()
