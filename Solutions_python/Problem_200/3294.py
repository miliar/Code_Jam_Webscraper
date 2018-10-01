cases = int(input())


def is_tidy(num):
    for i in range(len(num) - 1):
        if num[i] > num[i + 1]:
            return False
    return True


def comb(l):
    s = "".join([str(x) for x in l])
    return int(s)


def last_tidy(num):
    l_num = list(str(num))
    last = len(l_num) - 1
    for x in range(len(l_num)):
        l_num[x] = int(l_num[x])
    while not is_tidy(l_num) or not comb(l_num) <= num:
        if l_num[last] is not 0:
            l_num[last] -= 1
        else:
            l_num[last] = 9
            last -= 1
    return l_num


for i in range(cases):
    N = int(input())
    tidy = last_tidy(N)
    print("Case #{}: {}".format(i + 1, comb(tidy)))
