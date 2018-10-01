__author__ = 'thainguyen'

import math

# fi = open('MushroomMonster.in', 'r')
# fi = open('A-small-attempt0.in','r')
fi = open('A-large.in','r')
fo = open('MushroomMonster.out', 'w')

tests = int(fi.readline())
for test_case in range(tests):
    n = int(fi.readline())
    m = map(int,fi.readline().split())
    method1 = 0
    max_diff = 0
    for i in range(n-1):
        if m[i] > m[i+1]:
            method1 += m[i] - m[i+1]
        max_diff = max(max_diff, m[i]-m[i+1])
    rate = max_diff*1.0/10
    # print max_diff, rate
    method2 = 0
    for i in range(n-1):
        if m[i] < rate*10:
            method2 += m[i]
        else:
            method2 += rate*10
    method2 = int(method2)
    fo.write('Case #' + str(test_case+1) + ': ' + str(method1) + ' ' + str(method2) + '\n')