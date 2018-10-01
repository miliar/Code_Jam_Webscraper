#!/usr/bin/python

f = open('input.txt','r')
lines = f.readlines()
l = 0

def parseInt():
    global lines, l
    val = int(lines[l].strip())
    l += 1
    return val

def parseIntArray():
    global lines, l
    val = [ int(x) for x in lines[l].strip().split(' ') ]
    l += 1
    return val

def parseFloatArray():
    global lines, l
    val = [ float(x) for x in lines[l].strip().split(' ') ]
    l += 1
    return val

######################################################################
######################################################################
######################################################################
def solveCase(case_number, naomi, ken):
    n = len(naomi)
    naomi = sorted(naomi)
    ken = sorted(ken)
    merged = [0] * 2 * n

    # merge into a single list
    i = 0
    j = 0
    for index in xrange(0,2*n):
        if i == n:
            merged[index] = 'K'
            j += 1
        elif j == n:
            merged[index] = 'N'
            i += 1
        elif naomi[i] < ken[j]:
            merged[index] = 'N'
            i += 1
        else:
            merged[index] = 'K'
            j += 1

    # naomi fair play
    nseen = 0
    kscore = 0
    for owner in merged:
        if owner == 'N':
            nseen += 1
        elif owner == 'K':
            if nseen > 0:
                nseen -= 1
                kscore += 1

    naomi_fairplay_score = n - kscore

    # naomi deceitful war
    naomi_low = 0
    naomi_high = n - 1
    ken_low = 0
    ken_high = n - 1

    naomi_score = 0
    for i in xrange(n):
        if naomi[i] > ken[ken_low]:
            naomi_score += 1
            ken_low += 1

    naomi_cheating_score = naomi_score

    print 'Case #%d: %d %d' % (case_number, naomi_cheating_score, naomi_fairplay_score)

testcases = parseInt()
case_number = 1
for testcase in xrange(testcases):
    # parse the input
    n = parseInt()
    naomi = parseFloatArray()
    ken = parseFloatArray()

    # determine the correct card
    solveCase(case_number, naomi, ken)
    case_number += 1



