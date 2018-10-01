import sys
import numpy as np


def solve(cameron, jamie, test_case):
    
    if (len(cameron) + len(jamie) < 2) or (len(cameron) == len(jamie)):
        solution = 2
    else:
        actions = cameron if len(cameron) > 0 else jamie
        duration1 = max(b for a, b in actions) - min(a for a, b in actions)
        duration2 = min(b for a, b in actions) + (24*60) - max(a for a, b in actions)
        solution = 2 if min(duration1, duration2) <= 720 else 4
    
    print('Case #{}: {}'.format(test_case, solution))


def solve_all(fn):
    
    with open(fn) as f:
        T = int(f.readline().strip())
        for tc in range(1, T+1):
            AC, AJ = [int(x) for x in f.readline().strip().split()]
            cameron, jamie = [], []
            for i in range(AC):
                cameron.append([int(x) for x in f.readline().strip().split()])
            for i in range(AJ):
                jamie.append([int(x) for x in f.readline().strip().split()])
            solve(cameron, jamie, tc)


if __name__ == '__main__':
    solve_all(sys.argv[1])