#!/usr/bin/python
import sys
testcases = []
num_cases = None
max_score = 10
scores = range(1 + max_score)
totals = range(1 + 3 * max_score)
#
for each_line in open(sys.argv[1]):
    line = each_line.strip()
    if num_cases == None:
        num_cases = int(line)
    else:
        testcases.append(line)

#prefill testing tools
unsurprising = [-1 for _ in totals]
surprising   = [-1 for _ in totals]
for x in scores:
    if x +x +x  in totals:
        unsurprising[x +x +x] = x
    if (x +x +x-1  in totals) and (x-1 in scores):
        unsurprising[x +x +x-1] = x
    if (x +x-1 +x-1  in totals) and (x-1 in scores):
        unsurprising[x +x-1 +x-1] = x
    if (x +x +x-2  in totals) and (x-2 in scores):
        surprising[x +x +x-2] = x
    if (x +x-2 +x-2  in totals) and (x-2 in scores):
        surprising[x +x-2 +x-2] = x
    if (x +x-1 +x-2  in totals) and (x-2 in scores):
        surprising[x +x-1 +x-2] = x

#solve line
def solve(line):
    integers = line.split()
    N = int(integers.pop(0))
    S = int(integers.pop(0))
    p = int(integers.pop(0))
    t = [int(ti) for ti in integers]
    t_trimmed = []
    result = 0
    #unsurprising
    for each_total in t:
        if unsurprising[each_total] >= p:
            result +=1
        else:
            t_trimmed.append(each_total)#only interested in not unsurprising totals
    #surprising
    for each_total in t_trimmed:
        if surprising[each_total] >= p and S > 0:
            S -= 1
            result +=1
    return result
    

for index, testcase in enumerate(testcases):
    result = "Case #"+str(index+1)+": "
    result += str(solve(testcase))
    print result
