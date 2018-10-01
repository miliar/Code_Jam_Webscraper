import sys
from collections import deque

def get_testcases(file):
    lines = map(str.strip, file.readlines())

    n = int(lines[0])
    testcases = n*[None]
    for i in xrange(0, n):
        c = lines[(2*i)+1].split()
        d = lines[2*(i+1)]
        testcases[i] = {'R': int(c[0]), 'k': int(c[1]), 'N': int(c[2]), 'g': map(int, d.split())}
        # The roller coaster runs R times a day
        # The roller coaster can hold k people at once
        # There are N groups
    
    return testcases
    

def run_testcase(testcase):
    R, k, N, g = testcase['R'], testcase['k'], testcase['N'], testcase['g']
    queue = deque()

    r = 0 # revenue
    j = 0
    for i in xrange(0, R):
        while sum(queue) + g[j] <= k and len(queue) < N:
            queue.append(g[j])
            j = (j+1)%N
            
        #print '%d: %d' % (i, sum(queue))
        r += sum(queue)
        queue.clear()

    return r

testcases = get_testcases(sys.stdin)
for i, t in enumerate(testcases):
    print 'Case #%d: %d' % (i+1, run_testcase(t))