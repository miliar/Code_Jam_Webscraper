
t = int(raw_input())

for i in range(t):
    n, k = [int(s) for s in raw_input().split(" ")]
    l = 0
    tmp = k
    while tmp > 0:
        l += 1
        tmp /= 2
    l = 2 ** (l - 1)
    num = n / l
    flag = l - (num * l - n)
    if k > flag:
        dis = num - 1
    else:
        dis = num
    if dis % 2 == 0:
        mi = dis / 2 - 1
        ma = dis / 2
    else:
        mi = ma = (dis - 1) / 2
    print "Case #{}: {} {}".format(i + 1, ma, mi)

