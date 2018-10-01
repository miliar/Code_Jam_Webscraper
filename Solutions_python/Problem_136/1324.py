import fileinput
import re

WHITESPACE = re.compile("\s+")

def readlines():
    for line in fileinput.input():
        yield map(float, WHITESPACE.split(line.strip()))

def problems():
    lines = readlines()
    (T, ) = lines.next()
    for p in xrange(int(T)):
        (C,F,X) = lines.next()
        solve_problem(p,C,F,X)



def choices(C,F,X):
    ellapsed = 0.
    rate = 2.
    while True:
        # first solution, we stop building Farms
        yield ellapsed + (X / rate)
        # second solution, we build an extra farm
        ellapsed += C / rate
        rate += F

        



def solve_problem(p,C,F,X):
    res = float('inf')
    for x in choices(C,F,X):
        if x < res:
            res = x
        else:
            print "Case #%i: %f" % (p+1, res)
            break


        

problems()