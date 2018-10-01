#program to solve google code jam 2013 qualification round q. b (Lawnmower at https://code.google.com/codejam/contest/2270488/dashboard#s=p1)

import sys
#import some functions from another file
import bfuncs
from shlex import split
#getting input file
ARGS = sys.argv
FIN = open(ARGS[1], 'r')

#number of test cases
T = int(FIN.readline()[:-1])
print 'T:', T

#data extraction from input file
TESTCASES = []
for t in range(T):
    line_one = map(int, split(FIN.readline()[:-1]))
    N = line_one[0]
    M = line_one[1]
    FIELD = []
    for n in range(N):
        FIELD.append(map(int, split(FIN.readline()[:-1])))
    TESTCASES.append({'N': N, 'M': M, 'FIELD': FIELD})
print "TESTCASES:", TESTCASES

def main(testcase):
    if bfuncs.possible(testcase):
        return "YES"
    else:
        return "NO"

print "ANSWER:"
for t in range(T):
    print "Case #%i:" %(t+1), main(TESTCASES[t])

print "REMEMBER TO PUT AN EXTRA LINE ON THE END OF THE INPUT FILE SO THAT IT'S PARSED PROPERLY"
