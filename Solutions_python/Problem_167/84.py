from __future__ import print_function

import sys

fin = sys.stdin

num_cases = int(fin.readline().strip())

def pay(v, denoms, C, memo={}):
    params = (v, denoms, C)
    if params in memo:
        return memo[params]

    answer = False

    if v == 0:
        answer = True
    elif len(denoms) == 0:
        answer = False
    elif sum(denoms) * C < v:
        answer = False
    elif v < denoms[0]:
        answer = False
    else:
        for i in reversed(range(len(denoms))):
            if denoms[i] > v:
                continue
            for c in reversed(range(1,C+1)):
                if pay(v - (denoms[i] * c), denoms[:i], C):
                    answer = True
                    break

    memo[params] = answer
    return answer

def solve(C,V, denoms):
    l = len(denoms)
    v = 1
    while v < V+1:
        if not pay(v, denoms, C):
            denoms = tuple(list(denoms) + [v])
            v = v * (C+1)
        else:
            v += 1
    return len(denoms) - l


for t in range(num_cases):
    C,_,V = [int(x) for x in fin.readline().split()]
    denoms = tuple(int(x) for x in fin.readline().split())

    print("Case #{}: {}".format(t+1, solve(C,V,denoms)))