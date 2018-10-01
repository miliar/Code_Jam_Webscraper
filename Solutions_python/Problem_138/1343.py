#!/usr/bin/python3


for test_case in range(int(input())):
    print('Case #{}: '.format(test_case + 1), end='')
    n = int(input())
    a = list(sorted(map(float, input().split())))
    b = list(sorted(map(float, input().split())))
    b_copy = list(b)
    deceitful = 0
    for i in range(n):
        plus = 0
        for j in range(len(b)):
            if a[i] > b[j]:
                del b[j]
                plus = 1
                break
        deceitful += plus
    b = b_copy
    war = 0
    for i in range(n):
        plus = 1
        for j in range(len(b)):
            if b[j] > a[i]:
                del b[j]
                plus = 0
                break
        war += plus
    print('{} {}'.format(deceitful, war))