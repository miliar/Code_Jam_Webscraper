#!/usr/bin/python
cases = input()
for T in range(cases):
    n = input()
    inputString = raw_input()
    inputString = inputString.split()

    ans = 0.0
    for i in range(len(inputString)):
        if i != int(inputString[i])-1 :
            ans+=1

    print 'Case #%(T)d: %(ans).6lf'%{'T':T+1,'ans':ans}

