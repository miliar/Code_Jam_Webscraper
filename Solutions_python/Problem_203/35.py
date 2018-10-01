# coding: utf8

import sys
import copy


def main():
    T = int(sys.stdin.readline())
    for _T in range(T):
        R, C = map(int, sys.stdin.readline().split())
        cake = [
            list(sys.stdin.readline().strip())
            for _R in range(R)
        ]
        childs = []
        for i in range(R):
            for j in range(C):
                if cake[i][j] != '?':
                    childs.append([cake[i][j], i, i, j, j])
        for direction in (
                (-1, 0, 0, 0),
                (0, 0, -1, 0),
                (0, 1, 0, 0),
                (0, 0, 0, 1),
            ):
            for child in childs:
                while True:
                    tmp_child = child.copy()
                    for i in range(4):
                        tmp_child[1 + i] += direction[i]
                    if any(x < 0 or x >= R for x in tmp_child[1:3]):
                        break
                    if any(x < 0 or x >= C for x in tmp_child[3:5]):
                        break
                    collide = False
                    for i_child in childs:
                        if i_child[0] != tmp_child[0]:
                            if tmp_child[1] <= i_child[1] <= tmp_child[2] or i_child[1] <= tmp_child[1] <= i_child[2]:
                                if tmp_child[3] <= i_child[3] <= tmp_child[4] or i_child[3] <= tmp_child[3] <= i_child[4]:
                                    collide = True
                    if collide:
                        break
                    else:
                        child[1:5] = tmp_child[1:5]
        for child in childs:
            for i in range(child[1], child[2] + 1):
                for j in range(child[3], child[4] + 1):
                    cake[i][j] = child[0]
        print('Case #%s:' % (_T + 1))
        for row in cake:
            print(''.join(row))


if __name__ == '__main__':
    main()
