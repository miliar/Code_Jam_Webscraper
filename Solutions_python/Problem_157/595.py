import sys
from case_solve import solve_case

lines = sys.stdin.readlines()

testcases = int(lines[0])

lines = [l.rstrip() for l in lines[1:]]

results = []

i = 0
case = 1
while i < len(lines):
    chars, repeat = lines[i].split(' ')
    i += 1
    string = lines[i]
    i += 1
    print ("Case #%d: %s" % (case, solve_case(int(repeat), string)))
    print>>sys.stderr, ("Case #%d: %s" % (case, solve_case(int(repeat), string)))
    case += 1

