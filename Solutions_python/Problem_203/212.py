#!/usr/bin/env python3

T = int(input())

def solve(casei):
    line = input().split(" ")
    R = int(line[0])
    C = int(line[1])
    array = []
    for i in range(0, R):
        array.append(list(input()))

    for i in range(0, R):
        for j in range(0, C):
            ch = array[i][j]
            if ch == '?':
                continue
            for k in range(i+1, R):
                if array[k][j] == '?':
                    array[k][j] = ch
                else:
                    break
            for k in range(i-1, -1, -1):
                if array[k][j] == '?':
                    array[k][j] = ch
                else:
                    break

    for i in range(0, R):
        for j in range(0, C):
            ch = array[i][j]
            if ch == '?':
                continue
            for k in range(j+1, C):
                if array[i][k] == '?':
                    array[i][k] = ch
                else:
                    break
            for k in range(j-1, -1, -1):
                if array[i][k] == '?':
                    array[i][k] = ch
                else:
                    break

    print("Case #{}:".format(casei))
    for i in range(0, R):
        for j in range(0, C):
            print(array[i][j], end='')
        print()

for i in range(1, T+1):
    solve(i)
