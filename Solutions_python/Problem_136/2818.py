t = int(input())
for cycle in range(t):
    c, f, x = [float(i) for i in input().split()]
    flag = False
    cnt = 0
    farms = 0
    plus = 2
    res = 0
    while not flag:
        timeWithout = x / plus
        timeWith = c / plus + x / (plus + f)
        if timeWith < timeWithout:
            res += c / plus
            plus += f
        else:
            flag = True
            res += x / plus
    print("Case #", cycle + 1, ": ", res, sep="")