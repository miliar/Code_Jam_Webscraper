import sys
from collections import deque
from time import sleep

qty_test_cases = int(sys.stdin.readline())

for i in range(qty_test_cases):
    print "Case #%d:" % (i+1),
    
    test_case = sys.stdin.readline().strip().split(" ")
    #print test_case
    
    # extract combinations
    #print test_case[1:int(test_case[0])+2]
    combinations = dict([(x[0:2], x[2]) for x in test_case[1:int(test_case[0])+1]]) if int(test_case[0]) > 0 else {}
    test_case = test_case[int(test_case[0])+1:]
    #print combinations, test_case
    
    #extract opposites
    opposites = [tuple(x) for x in test_case[1:int(test_case[0])+1]] if int(test_case[0]) > 0 else []
    test_case = test_case[int(test_case[0])+1:]
    #print opposites, test_case
    
    invocation_queue = deque(test_case[1][0:int(test_case[0])])
    result = ""
    
    while len(invocation_queue) > 0:
        result += invocation_queue.popleft()
        
        if result[-2:] in combinations.keys():
            result = result[0:-2] + combinations[result[-2:]]
        elif result[-2:][::-1] in combinations.keys():
            result = result[0:-2] + combinations[result[-2:][::-1]]
        
        for possible_opposite in filter(lambda x: result[-1] in x, opposites):
            #print possible_opposite
            try:
                find_elem = possible_opposite[0] if result[-1] == possible_opposite[1] else possible_opposite[1]
            except IndexError:
                pass
            #print "AAAA", repr(find_elem), repr(result[0:-1])
            if find_elem in result[0:-1]:
                result = ""
        
    
    print "[" + ", ".join(list(result)) + "]"