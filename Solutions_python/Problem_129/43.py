import math

tcs = int(input())

for tc in range(1, tcs+1):
    n, m = (int(i) for i in input().split(' '))

    full = 0

    enter = dict()
    exit = dict()

    for i in range(m):
        o, e, p = (int(i) for i in input().split(' '))
        enter[o] = enter.get(o, 0) + p
        exit[e] = exit.get(e, 0) + p
        full += p * ((e - o) * n - (e - o) * (e - o - 1) / 2)
        #full %= 1000002013

    enter = sorted(enter.items())
    exit = sorted(exit.items())

    i = 0
    j = 0

    queue = list()
    cost = 0

    while j < len(exit):
        if i < len(enter) and enter[i][0] <= exit[j][0]:
            # Make some passengers enter
            queue = enter[i][1] * [enter[i][0]] + queue
            i += 1
        else:
            # Make some passengers exit
            e = exit[j][0]
            for o in queue[:exit[j][1]]:
                cost += (e - o) * n - (e - o) * (e - o - 1) / 2
                #cost %= 1000002013
            queue = queue[exit[j][1]:]
            j += 1

    print("Case #%d: %d" % (tc, (1000002013 + full - cost) % 1000002013))
