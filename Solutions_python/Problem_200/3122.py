#! /usr/bin/python3

def correct(x):
    for i in range(len(x)-1):
        if x[i] > x[i+1]:
            x[i] = str(int(x[i])-1)
            for j in range(i+1, len(x)):
                x[j] = '9'
            break
    return x

tc = int(input().strip())

for t in range(tc):

    from collections import deque

    n = int(input().strip())

    x = list(str(n))

    while(x != sorted(x)):
        x = correct(x)

    res = int(''.join(x))
    print('Case #{}: {}'.format(t+1, str(res)))
