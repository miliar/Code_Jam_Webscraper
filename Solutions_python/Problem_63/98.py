import sys
import math

def load_testing(L, P, C):

    #print 'LPC', L, P, C
    
    
    if L*C >= P:
        return 1
    else:
        return 1 + load_testing(L*C, P, C)
    
    
    
    #return 1


if __name__ == '__main__':
    ntests = int(sys.stdin.readline())
    for i in range(1, ntests+1):
        L, P, C = map(int, sys.stdin.readline().strip().split())
        ans = int(math.ceil(math.log(load_testing(L, P, C), 2)))
        print 'Case #%s: %s' %  (i, ans)
