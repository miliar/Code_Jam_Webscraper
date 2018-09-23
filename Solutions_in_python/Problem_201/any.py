# -*- coding: utf-8 -*-

import sys
import os
import math
import heapq

input_text_path = __file__.replace('.py', '.txt')
fd = os.open(input_text_path, os.O_RDONLY)
os.dup2(fd, sys.stdin.fileno())

T = int(input())
f = open('submit.txt', 'w')

for i in range(T):
    print(i, T)
    N, K = map(int, input().split())
    #print(N, K)
    # N stall
    # K people

    # heap
    A = []
    heapq.heappush(A, -N)

    half0 = None
    half1 = None
    for _ in range(K):
        max_len = -heapq.heappop(A)
        max_len -= 1
        half0 = max_len // 2
        half1 = max_len - half0
        heapq.heappush(A, -half0)
        heapq.heappush(A, -half1)
    s = 'Case #{}: {} {}\n'.format(i+1, max(half0, half1), min(half0, half1))
    f.write(s)
f.close()




