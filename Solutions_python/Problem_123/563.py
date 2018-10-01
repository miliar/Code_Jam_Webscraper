import sys
import math
import decimal

T = int(sys.stdin.readline())

for i in range(T):

    A, N = map(int, sys.stdin.readline().strip().split(' '))
    sizes = map(int, sys.stdin.readline().strip().split(' '))
    sorted_sizes = sorted(sizes)
    
    if A == 1:
        print "Case #" + str(i+1) + ": " + str(N)
    else:
        cnt = 0
        for idx, s in enumerate(sorted_sizes):
            buf_cnt = 0
            if A <= s:
                buf_cnt = int(math.floor(math.log((s-1),2) - math.log((A-1),2)) + 1)
                A = pow(2, buf_cnt)*(A-1)+1
            if buf_cnt >= N - idx:
                cnt += N - idx
                break
            else:
                A += s
                cnt += buf_cnt
                    
        
        print "Case #" + str(i+1) + ": " + str(cnt)
