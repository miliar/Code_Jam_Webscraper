def is_tidy(num):
    l = list(map(int, str(num)))
    return all(map(lambda x: x[0] <= x[1], zip(l, l[1:])))


def is_monotonic_decreasing(num):
    l = list(map(int, str(num)))
    return all(map(lambda x: x[0] >= x[1], zip(l, l[1:])))


def remove_monotonic_decreasing_part(num):
    l = list(str(num))
    return int(''.join(l)) - int(''.join(l[1:])) - 1


def remove_tail(num):
    l = list(str(num))
    i = 0
    while l[i] <= l[i + 1] and i + 1 < len(l):
        i += 1
    return int(''.join(l)) - int(''.join(l[i + 1:])) - 1

cases = int(input())
for case in range(1, cases + 1):
    num = int(input())

    while num:
        if is_tidy(num):
            print('Case #{}: {}'.format(case, num))
            break
        elif is_monotonic_decreasing(num):
            num = remove_monotonic_decreasing_part(num)
        else:
            num = remove_tail(num)


TC = """
8
171111111111111110
119111191111111110
132
1000
7
111111111111111110
912932112332112311
999998888833333999
"""