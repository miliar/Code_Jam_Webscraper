#
# Google Code Jam 2011
# Roaund 0: A. Bot Trust
# submission by EnTerr
#

'''
Input 
3
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1

Output 
Case #1: 6
Case #2: 100
Case #3: 4
'''

import sys
#import psyco
#psyco.full()

f = open(sys.argv[1])
def input(): return f.readline().strip();


def bot_thrust(seq):
    t = 0
    rt = [0,0] # times
    rx = [1,1] # positions
    while seq:
        r = 0 if seq.pop(0)=='O' else 1
        x = int(seq.pop(0))
        # how many steps we need: abs(x-rx[r])
        # how much "free time" we have: t-rt[r]
        dt = max(0, abs(x-rx[r]) - (t-rt[r])) + 1
        t += dt
        rx[r] = x
        rt[r] = t
        # print r, rx[r], rt[r]
        
    return t

for caseNo in range(1, int(input())+1):
    print 'Case #%d: %d' % (caseNo, bot_thrust(input().split()[1:]))

