# Google Code Jam 2011 round 1A.
# D = #played today
# Dwon = #won today
# G = #played ever
# Gwon = #won ever
# Pd, Pg = percent won today, ever
# Dwon = Pd * .01 * D
# Gwon = Pg * .01 * G
# Is there an integer D < N s.t. isinteger(Dwon)
# and integer G s.t. isinteger(Gwon)
# and Gwon >= Dwon
# What's the bound for searching G?
# G * Pg is divisible by 100.
# Can add multiples of Pg until div 100.
# Oh, Pg * n * 100 is divisible by 100!  So Pg can be ignored.
# Can add up to N multiples of Pd until div 100.
# That's lots of additions to get to 10**15.
# Oh, we probably cycle before then?
# Again, Pd * n * 100 is divisible by 100, so big Ns aren't a problem.

from collections import deque   # Faster to delete at front
import sys
def doCase(N, Pd, Pg):
    if Pg == 100 and Pd != 100: return 'Broken'
    if Pg == 0 and Pd > 0: return 'Broken'
    total = Pd
    for i in range(min(N,101)):
        if total % 100 == 0: return 'Possible'
        total += Pd
    return 'Broken'

def run():
    file = open(sys.argv[1])
    numCases = int(file.readline())
    for case in range(1, numCases+1):
        (N,Pd,Pg) = file.readline().split()
        answer = doCase(int(N), int(Pd), int(Pg))
        print 'Case #{0}: {1}'.format(case, answer)
run()
