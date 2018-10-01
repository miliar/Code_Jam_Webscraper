# -*- coding: utf-8 -*-

import sys

def solve(N, K):
    # print N,K
    if K == 1:
        if N % 2 == 1:
            return (N//2, N//2)
        return  (N//2, N//2-1)
    if N % 2 == 0:
        if K % 2 == 0:
            return solve(N//2,K//2)
        else:
            return solve(N//2-1,K//2)
    else:
        return solve(N//2, K//2)


if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename) as f:
        n_cases = int(f.readline())
        for i in xrange(n_cases):
            N, K = map(int,f.readline().split())
            x,y = solve(N, K)
            print 'Case #{}: {} {}'.format(i+1,x,y)
        
