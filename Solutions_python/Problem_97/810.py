from collections import deque
from string import rstrip
from sys import stdin, stdout

input = []
for line in stdin: input.append(rstrip(line,'\n'))
nTestCases = int(input.pop(0))
testcase = 1

while True:
    stdout.write("Case #%s: "%testcase)
    tokens = input[testcase-1].split(' ')
    A = int(tokens.pop(0))
    B = int(tokens.pop(0))
    dr = 0
    for n in xrange(A,B+1):
        sn = deque(str(n))
        osn = ''.join(list(sn))
        sn.rotate(1)
        while ''.join(list(sn)) != osn:
            if A <= n < int(''.join(list(sn))) <= B: dr += 1
            sn.rotate(1)

    stdout.write(str(dr)+"\n")
    if testcase >= nTestCases: break
    testcase +=1

