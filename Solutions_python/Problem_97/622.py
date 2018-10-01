#!/usr/bin/python
import sys
#init
num_cases = None
testcases = []

#read file and get num_cases and all test cases
for each_line in open(sys.argv[1]):
    line = each_line.strip()
    if num_cases == None:
        num_cases = int(line)
    else:
        testcases.append([int(value) for value in line.split()])

#solve case
def solve(testcase):
    start, end = testcase
    num_len = len(str(start))
    possibilities = dict(zip(range(start,end+1),[[] for _ in range(start,end+1)]))
    for original in possibilities:
        possibilities[original] = get_recycled(original, start, end)
    return sum([len(possibilities[num]) for num in possibilities])
    
def get_recycled(original, start, end):
    recycled = [original]
    str_original = str(original)
    str_variant = str_original
    for _ in range(len(str_original) -1):
        str_variant = str_variant[1:] + str_variant[0]
        if str_variant[0] != "0":
            variant = int(str_variant)
            if variant not in recycled and variant > original:
                if start <= variant <= end:
                    recycled.append(variant)
    return recycled[1:]
  
for index, testcase in enumerate(testcases):
    result = "Case #"+str(index+1)+": "
    result += str(solve(testcase))
    print result
