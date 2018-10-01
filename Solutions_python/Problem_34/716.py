import sys
import re

L, N, D = [int(x) for x in sys.stdin.readline().split()]

knowneds = []
for i in xrange(N):
    knowneds.append( sys.stdin.readline() )

str_knowneds = '\n'.join(knowneds)

unknowneds = []
for i in xrange(D):
    unknowneds.append( sys.stdin.readline() )

def count(case):
    pattern = case.replace('(','[').replace(')',']')
    return len( re.findall(pattern, str_knowneds) )

for i, case in enumerate(unknowneds):
    print "Case #%d: %d" % (i+1, count(case))
