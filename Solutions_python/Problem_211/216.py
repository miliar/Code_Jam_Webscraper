from collections import Counter
import math
import fnmatch


T = int(raw_input().strip())
for i in range(T):
    doPrint = False
    temp = map(int, raw_input().strip().split(" "))
    N = temp[0] # units
    K = temp[1] # units to operate
    U = float(raw_input().strip()) # training units
    probs = sorted(map(float, raw_input().strip().split(" ")))
    if doPrint: print "N, K, U, probs = ", N, K, U, probs

    for j in range(1, N):
        if probs[j] > probs[j-1]:
            increase = min(U/j, probs[j]-probs[j-1])
            for k in range(j):
                probs[k] += increase
            U -= j * increase
    
    if U > 0:
        for j in range(N):
            probs[j] += U / N
     
    if doPrint: print "probs = ", probs       

    answer = 1
    for j in range(N):
        answer *= probs[j]
    if doPrint: print "answer = ", answer
            
    if doPrint: print " "
    if doPrint == False: print "case #" + str(i+1) + ": " + str(answer)
    