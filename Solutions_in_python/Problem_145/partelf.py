import sys
import math
import fractions

def problem_instances(filename):
    f = open(filename)
    num_instances = int(f.readline())
    for i in range(num_instances):
        yield map(int, f.readline().split("/"))

def solve(instance):
    P, Q = instance
    if P == Q:
        return 0

    frac = fractions.Fraction(P, Q)
    gencount = 0

    while True:
        lg = int(math.log(frac.denominator, 2))
        if frac.denominator != 2 ** lg:
            return "impossible"

        if frac.numerator * 2 >= frac.denominator:
            return gencount + 1
        frac = fractions.Fraction(frac.numerator * 2, frac.denominator)
        gencount += 1


filename = sys.argv[1]
out = open(filename + ".out", "w")
for idx, instance in enumerate(problem_instances(filename), 1):
    out.write("Case #%i: %s\n" % (idx, solve(instance)))