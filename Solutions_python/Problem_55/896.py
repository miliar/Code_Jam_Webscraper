# roller-coaster.py

import sys, io

assert len(sys.argv) >= 2
data = [ string.replace('\n','') for string in (io.open(sys.argv[1])).readlines()]

testcases = data[0]
data = data[1:]

def split_testcases(data):
    '''Splits testcases into a list of dictionaries'''
    length = len(data)
    testcases = []
    for i in range(0, length, 2):
        d = {}
        vars = [int(number) for number in data[i].split(" ")]
        d['times'] = vars[0]
        d['cap'] = vars[1]
        d['groups'] = [int(num_people) for num_people in data[i + 1].split(" ")]
        testcases.append(d)
    return testcases

def get_first(max, list):
    _sum = 0
    n = 0
    for number in list:
        _sum += number
        if _sum > max:
            #print "SUM"
            #print "N: {0}".format(n)
            return sum(list[:n]), list[n:] + list[:n]
        n += 1
    return sum(list[:n]), list[n:] + list[:n]

testcase_number = 1

for testcase in split_testcases(data):
    cap = testcase['cap']
    times = testcase['times']
    groups = testcase['groups']
    profit = 0
    
    #print "===Testcase #{0}".format(testcase_number)
    #print "   Max pass.: {0}".format(cap)
    #print "   Times: {0}".format(times)
    #print "   Groups: " + str(groups)
    
    for i in range(0, times):
        earn, groups = get_first(cap, groups)
        profit += earn
    
    print "Case #{0}: {1}".format(testcase_number, profit)
    testcase_number += 1
