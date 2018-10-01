import sys

T = int(sys.stdin.readline())

for case in range(1,T+1):
    [A,B,K] = map(int, sys.stdin.readline().split())
    count = 0
    for i in range (0,A):
        for j in range(0,B):
            if ( (i & j) < K):
                count = count + 1
#                 print (i,j)
                
    print "Case #" + str(case) + ": " +  str(count)