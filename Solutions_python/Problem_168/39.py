#!/usr/bin/env python3.4
import sys
import math

def convert_dir(x):
    if x == '.':
        return 0
    elif x == '^':
        return 1
    elif x == '>':
        return 2
    elif x == 'v':
        return 3
    else:
        return 4

if __name__ == '__main__':
    for test_case in range(int(sys.stdin.readline())):
        sys.stdout.write('Case #{}: '.format(test_case + 1))
        rows, cols = map(int, sys.stdin.readline().split())
        mat = []
        constraints = dict()
        for r in range(rows):
            line = list(map(convert_dir, sys.stdin.readline().strip()))
            mat.append(line)
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] != 0:
                    constraints.setdefault((r, c), [])
                    constraints[(r, c)].append(4)
                    break
        for r in range(rows):
            for c in range(cols - 1, -1, -1):
                if mat[r][c] != 0:
                    constraints.setdefault((r, c), [])
                    constraints[(r, c)].append(2)
                    break
        for c in range(cols):
            for r in range(rows):
                if mat[r][c] != 0:
                    constraints.setdefault((r, c), [])
                    constraints[(r, c)].append(1)
                    break
        for c in range(cols):
            for r in range(rows - 1, -1, -1):
                if mat[r][c] != 0:
                    constraints.setdefault((r, c), [])
                    constraints[(r, c)].append(3)
                    break
        cnt = 0
        for k, v in constraints.items():
            if len(v) == 4:
                print('IMPOSSIBLE')
                break
            else:
                if mat[k[0]][k[1]] in v:
                    cnt += 1
        else:
            print(cnt)

