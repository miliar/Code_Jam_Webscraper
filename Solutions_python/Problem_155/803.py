import sys

#
# Google codejam Qualification Round 2015 Problem A. Standing Ovation
# https://code.google.com/codejam/contest/6224486/dashboard
# 
# Solved by Amy
#
# read & parse input file
inputFile = open('A-large.in.txt')
cases = []
n = 0
for line in inputFile:
    if n == 0:
        n = int(line.strip())
    else:
        case = line.strip()
        cases.append(case)

# check one case 
def check(case):
    spl = case.strip().split(' ')
    smax = int(spl[0])
    s = spl[1]

    count = int(s[0])   # total number of people on previous shyness levels
    result = 0  # people needed

    for i in range(1, smax + 1):
        levelcnt = int(s[i])    # how many people in the audience have shyness level i
        level = i   # total audience needed for people on shyness level i to applaud
        if  count < level:
            dif = level - count
            result += dif
            #s[0] = int(s[0]) + dif
            count += levelcnt + dif
        else:
            count += levelcnt
    return result   
 
# output
for c in range(n):
    case = cases[c]
    out = int(check(case))
    print 'Case #%d: %d' %(c + 1, out)
     
# end