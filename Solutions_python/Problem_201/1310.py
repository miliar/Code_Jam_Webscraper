def func(n, k):
    dic = {}
    dic[n] = 1
    now = 0

    while now < k:
        x = sorted(dic, reverse = True)[0]
        y = dic[x]

        max_value = int(x / 2)
        min_value = int((x - 1) / 2)

        dic.pop(x)

        if (now + y) >= k:
            return (max_value, min_value)

        if max_value in dic:
            dic[max_value] = dic[max_value] + y
        else:
            dic[max_value] = y

        if min_value in dic:
            dic[min_value] = dic[min_value] + y
        else:
            dic[min_value] = y

        now += y
    return (0, 0)


t = int(input())

for i in range(1, t + 1):
    n, k = [int(s) for s in input().split(" ")]
    max_R, min_R = func(n, k)
    print("Case #{}: {} {}".format(i, max_R, min_R))
