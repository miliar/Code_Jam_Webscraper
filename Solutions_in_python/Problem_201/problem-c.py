import os
import sys
import numpy as np
import sys
sys.setrecursionlimit(10000)


def solve_rec(Ns, K):
    N = max(Ns)
    Ns.remove(N)
    if N % 2 == 0:
        if K == 1:
            return N//2, N//2 - 1
        Ns.extend([N//2, N//2-1])
    else:
        if K == 1:
            return N//2, N//2
        Ns.extend([N//2, N//2])
    return solve_rec(Ns, K-1)

def solve(N, K):
    return solve_rec([N], K)

if __name__ == '__main__':
    try:
        input = sys.argv[1]
    except:
        input = os.path.join('data', 'input.txt')
    output = os.path.join('data', 'output.txt')
    with open(input, 'r') as fin:
        with open(output, 'w') as fout:
            num_cases = int(fin.readline())
            for case in range(num_cases):
                fout.write('Case #%d: ' % (case+1))
                line = fin.readline().split(' ')
                N = int(line[0])
                K = int(line[1])
                res = solve(N, K)
                fout.write(str(res[0]) + ' ' + str(res[1]) + '\n')
