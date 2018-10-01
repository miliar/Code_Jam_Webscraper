__author__ = 'bszikszai'

from io import *

def solve(f):
    ctr = [int(x) for x in list(f.readline().rstrip('\n').rstrip('\r').split(' ')[1])]
    print ctr
    sum = 0
    req = 0
    for (i,x) in enumerate(ctr):
        if i <= sum:
            sum += x
        if x != 0 and i > sum:
            req += i - sum
            #print "At %s added %s" % (i, (i-sum))
            sum += i - sum + x
            #print "Has %s" % (sum)
    return req

with open('input.txt', 'r') as f:
    with open('output.txt', 'wb') as g:
        cases = int(f.readline())
        for i in range(0, cases):
            solution = solve(f)
            print "Case #%s: %s" % (i+1, solution)
            g.write("Case #%s: %s\n" % (i+1, solution))