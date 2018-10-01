t = int(raw_input())
count = 1
while t != 0 :
    n = raw_input()
    res = int(n)
    flag = 0
    while flag != 1:
        p = list(str(res))
        if p == sorted(p):
            flag = 1
        else:
            res = res - 1
    print "Case #{}: {}".format(count, res)
    count = count + 1
    t = t - 1
