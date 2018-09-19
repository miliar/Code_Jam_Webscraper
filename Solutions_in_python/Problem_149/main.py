T = int(input())
test = 1

swap = 0


def count_sort(l):
    global swap
    if len(l) < 2:
        return l
    else:
        mid = len(l) // 2
        l1 = count_sort(l[0:mid])
        l2 = count_sort(l[mid:])
        a = b = 0
        ret = []
        while a < len(l1) and b < len(l2):
            if l1[a] < l2[b]:
                ret.append(l1[a])
                a += 1
            else:
                swap += mid - a
                ret.append(l2[b])
                b += 1
        while a < len(l1):
            ret.append(l1[a])
            a += 1
        while b < len(l2):
            ret.append(l2[b])
            b += 1
        return ret


def count_swap(l):
    global swap
    # print(l)
    swap = 0
    count_sort(l)
    return swap


def try_inv(l, i):
    if i == len(l):
        return count_swap(l)
    count = try_inv(l, i + 1)
    l[i] = 10000 - l[i]
    new_count = try_inv(l, i+1)
    return min(count, new_count)


while test <= T:
    print("Case #" + str(test) + ": ", end="")
    test += 1
    size = int(input())
    l = [int(i) for i in input().split()]
    sorted_l = sorted(l)
    new_l = [sorted_l.index(i) for i in l]
    #print(new_l)
    print(try_inv(new_l, 0))