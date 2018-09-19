#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Sreyantha Chary
#
# Created:     13/04/2013
# Copyright:   (c) Sreyantha Chary 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def ver_check(m ,lines, N):
    for n in range(N):
        if lines[n][m] == '2':
            return False
    return True

def hor_check(n ,lines, M):
    for m in range(M):
        if lines[n][m] == '2':
            return False
    return True

def get_answer(lines, N, M):
    for m in range(M):
        if lines[0][m] == '1' or lines[0][m] == 'x':
            if ver_check(m, lines, N):
                for n in range(N):
                    lines[n][m] = 'x'

    for n in range(N):
        if lines[n][0] == '1' or lines[n][0] == 'x':
            if hor_check(n, lines, M):
                for m in range(M):
                    lines[n][m] = 'x'

    for line in lines:
        if '1' in ''.join(line):
            return "NO"
    return "YES"

##    for m in range(M):
##        if lines[0][m] == '1' or lines[0][m] == 'x':
##            if check(0, m, lines) == 'v':
##                for n in range(N):
##                    lines[n][m] = 'x'
##            elif check(0, m , lines) == 'h':
##                for m1 in range(M):
##                    lines[0][m1] = 'x'

test_cases = int(raw_input())



for i in range(test_cases):
    line = raw_input()
    [N, M] = line.split(' ')
    lines = []
    for j in range(int(N)):
        lines.append(raw_input().split(' '))
    print "Case #%s: %s" % (str(i+1), get_answer(lines, int(N), int(M)))
