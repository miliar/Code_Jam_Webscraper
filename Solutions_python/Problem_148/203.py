t = int(input())
for tc in range(1, t+1):
    (n, x) = [int(tmp) for tmp in input().split()]
    slist = [int(tmp) for tmp in input().split()]
    slist.sort()
    y = 0
    while slist != []:
        xr = x - slist.pop()
        if slist != []:
            if slist[-1] <= xr:
                slist.pop()
            else:
                for i in range(0, len(slist)):
                    if slist[i] > xr:
                        if i == 0:
                            break
                        del slist[i-1]
                        break
        y += 1
    print('Case #%i: %i' % (tc, y))
