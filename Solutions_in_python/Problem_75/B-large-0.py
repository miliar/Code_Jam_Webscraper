#! /usr/bin/env python

# by Andrew Szeto
# Problem B large

testfile = open("B-large-0.in").read().split('\n')
T = int(testfile[0])

for num in xrange(1, T+1):
    case = testfile[num].split(' ')
    C = int(case[0])
    combinations1 = [item[0:2] for item in case[1:C+1]] if C else list()
    combinations2 = [item[2] for item in case[1:C+1]] if C else list()
    D = int(case[C+1])
    cancels = [item for item in case[C+2:-2]] if D else list()
    N = case[-1]
    answer = list()
    for letter in N:
        answer.append(letter)
        if len(answer) >= 2:
            twofer = ''.join((answer[-2],answer[-1]))
            if twofer in combinations1:
                answer.pop()
                answer.pop()
                answer.append(combinations2[combinations1.index(twofer)])
                continue
            if twofer[::-1] in combinations1:
                answer.pop()
                answer.pop()
                answer.append(combinations2[combinations1.index(twofer[::-1])])
                continue
            for x in cancels:
                if x[0] in answer and x[1] in answer:
                    answer = list()
    print "Case #%s: [%s]" %(num, ', '.join(answer))
