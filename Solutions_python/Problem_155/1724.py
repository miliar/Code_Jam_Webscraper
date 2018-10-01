__author__ = "TitanUser"

total = int(input())

for i in range(0, total):
    raw = input().split(' ')
    l = int(raw[0])
    s = 0
    res = 0

    for j in range(0, l+1):
        if s < j+1:
            res += 1
            s += 1
        s += int(raw[1][j])
    print("Case #{0}: {1}".format(i+1, res-1))
