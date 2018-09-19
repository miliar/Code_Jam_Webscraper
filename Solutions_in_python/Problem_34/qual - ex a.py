import re

f = open('A-large.in')
params = f.readline()
L, D, N = params.split()
L = int(L)
D = int(D)
N = int(N)
temp = []
for line in f:
    temp.append(line.strip('\n').replace('(', '[').replace(')', ']'))

words = temp[:D]
test_cases = temp[D:]
case_number = 0
matches_at_case = []
for case in test_cases:
    valid = re.compile(case)
    matches_at_case.append(0)
    for word in words:
        if valid.match(word) != None:
            matches_at_case[case_number] += 1
    case_number += 1

for i in range(len(matches_at_case)):
    print "Case #%d: %d" % (i+1, matches_at_case[i])