from string import rstrip
from sys import stdin, stdout

input = []
for line in stdin: input.append(rstrip(line,'\n'))
nTestCases = int(input.pop(0))
testcase = 1

while True:
    stdout.write("Case #%s: "%testcase)
    tokens = input[testcase-1].split(' ')
    tokens = [int(token) for token in tokens]
    N = tokens.pop(0)
    S = tokens.pop(0)
    P = tokens.pop(0)
    #print N, S, P, tokens
    nb = 0
    i = 0
    while 1:
        if i>=len(tokens): break
        if tokens[i] < P:
            pass
        elif tokens[i]>=3*P-2:
            nb += 1
            tokens.pop(i)
            continue
        elif S and tokens[i] >= 3*P-4:
            nb += 1
            tokens.pop(i)
            S-=1
            continue
        i+=1
    stdout.write(str(nb)+"\n")
    if testcase >= nTestCases: break
    testcase +=1

