[t, ] = [int(x) for x in input().split()]
from copy import copy

def process_test(num):
    [r, c] = [int(x) for x in input().split()]
    mymap = []
    for i in range(r):
        mymap.append(list(input()))

    for i in range(len(mymap)):
        jump = 0
        while all([x == '?' for x in mymap[i+jump]]):
            jump += 1
            if i + jump >= len(mymap):
                jump = -1
        mymap[i] = copy(mymap[i+jump])

        j = 0
        while mymap[i][j] == '?':
            j += 1
        last_ini = mymap[i][j]
        mymap[i][:j] = last_ini * (j)
        j += 1
        while j < len(mymap[i]):
            if mymap[i][j] == '?':
                mymap[i][j] = last_ini
            else:
                last_ini = mymap[i][j]
            j += 1

    print("Case #", num, ": ", sep='')
    for row in mymap:
        print(''.join(row))

for num in range(1, t+1):
    process_test(num)