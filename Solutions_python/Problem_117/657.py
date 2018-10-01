'''
Created on 13/04/13
Code Jam 2013 Qualification Round B
@author: manolo
'''

import sys
ifile = sys.stdin
def r():
    return ifile.readline()[:-1]

ofile = open('./b-small.out', 'w')
def w(what):
    ofile.write(what + '\n')

def all_the_same(line):
    check_later = []
    for i in range(len(line)):
        if not line[0] == line[i]:
            check_later.append(i)
    return check_later

def all_the_same_2(line):
    check_later = []
    all_same = True
    for i in range(len(line)):
        all_same = all_same and line[i] == line[0]
        if line[i] == 1:
            check_later.append(i)
    if all_same:
        return []
    else:
        return check_later

def check_columns(numbers, columns):
    for c in columns:
        print 'checking column ' + str(c)
        col = []
        for i in range(len(numbers)):
            col.append(numbers[i][c])
        for n in col:
            print '                      ' + str(n)
    
        conflicts = all_the_same(col)
        if len(conflicts) > 0:
            print 'column ' + str(col) + ' has conflicts in rows' + str(conflicts)
            return False
        else:
            print 'column ' + str(col) + ' is ok'
    print
    return True

def solve_test(numbers):

    print 'numbers:'
    for row in numbers:
        print row

    check_later = []
    for row in numbers:
        conflicts = all_the_same_2(row)
        check_later.extend(conflicts)
        if len(conflicts) == 0:
            print 'row ' + str(row) + ' is ok'
        else:
            print 'row ' + str(row) + ' has conflicts in columns ' + str(conflicts)
    
    check_later = set(check_later)
    print 'check later: ' + str(check_later)
    print
    
    return check_columns(numbers, check_later)

t = int(r())
print 't: ' + str(t)

for test in range(t):
    print 'test: ' + str(test+1)
    (N, M) = r().split(' ')
    n = int(N)
    m = int(M)
    print str(n) + ", " + str(m)
    
    numbers = [None] * n
    for i in range(n):
        numbers[i] = [int(x) for x in r().split(' ')]
        
    solvable = solve_test(numbers)
    w('Case #' + str(test+1) + ': ' + ('YES' if solvable else 'NO'))


ofile.close

