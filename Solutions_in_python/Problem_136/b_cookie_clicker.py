'''
Created on Apr 13, 2014

@author: Kevin
'''
import sys

def solve(case):
    C = case[0]
    F = case[1]
    X = case[2]
    elapsed = 0.0
    production = 2.0  # Per hour
    current_time = elapsed + X/production
    while(True):
        time_upgrade = elapsed + C/production + X/(production+F)
        if (current_time <= time_upgrade):
            return "%.7f" % current_time
        else:
            elapsed = elapsed + C/production
            current_time = time_upgrade
            production = production + F


# Main program
filename = "B-large"
fin = open("%s.in" % filename)
sys.stdout = open("%s.out" % filename, "w")

numcases = int(fin.readline())
for casenum in range(1, numcases + 1):
    row_str = fin.readline()
    case_info = [float(x) for x in row_str.split()]
    print "Case #%d: %s" % (casenum, solve(case_info))
