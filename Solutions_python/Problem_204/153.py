#!/usr/bin/env python3

import sys
import math

def calc_servings(package_size, serv_size):
    lo_size = math.ceil(package_size / serv_size / 1.1)
    hi_size = math.floor(package_size / serv_size / 0.9)
    return lo_size, hi_size
'''
    lo_serv_size = serv_size - (serv_size // 10)
    hi_serv_size = serv_size + (serv_size // 10)

    lo_size = package_size // hi_serv_size
    hi_size = package_size // lo_serv_size

    while lo_size * hi_serv_size < package_size:
        lo_size += 1
    while hi_size * lo_serv_size > package_size:
        hi_size -= 1

    return lo_size, hi_size
'''

def solve(N, P, R, Q):
    for i in range(N):
        Q[i].sort(reverse=True)

    total_created = 0
    finished = False

    while not finished and Q[0]:
        pkg0 = Q[0].pop()
        min_s0, max_s0 = calc_servings(pkg0, R[0])
        #print('pkg0:', pkg0, 'serving size:', R[0], 'gives:', min_s0, max_s0, file=sys.stderr)
        if min_s0 > max_s0:
            continue

        for test_s in range(min_s0, max_s0+1):
            found_s = True
            found_indexes = [-1]
            for i in range(1, N):
                found_i = False
                for j in range(len(Q[i])-1, -1, -1):
                    pkg = Q[i][j]
                    min_si, max_si = calc_servings(pkg, R[i])
                    if min_si <= test_s <= max_si:
                        found_i = True
                        found_indexes.append(j)
                        break
                if not found_i:
                    found_s = False
                    break
            if found_s:
                #print('for test_s', test_s, 'found_indexes', found_indexes, file=sys.stderr)
                for i in range(1, N):
                    Q[i].pop(found_indexes[i])
                total_created += 1
                break

    return total_created

T = int(input())
for t in range(T):
    N, P = map(int, input().split())
    R = list(map(int, input().split()))
    Q = [list(map(int, input().split())) for _ in range(N)]
    #print(file=sys.stderr)
    #print('Case #{}:'.format(t+1), file=sys.stderr)
    #print('N =', N, 'P =', P, file=sys.stderr)
    #print('R =', R, file=sys.stderr)
    #print('Q =', Q, file=sys.stderr)
    res = solve(N, P, R, Q)
    print('Case #{}: {}'.format(t+1, res))

