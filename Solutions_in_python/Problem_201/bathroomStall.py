def increment(d, l, index):
    if index in d:
        d[index] += 1
    else:
        d[index] = 1
        l.append(index)
        l.sort()


def occupy(s):
    num_stalls, num_people = [int(x) for x in s.split(" ")]
    free, free_index = dict(), []
    free[num_stalls] = 1
    free_index.append(num_stalls)

    count = 1
    while count <= num_people:
        #print("free_index: ", free_index)
        #print("free: ", free)

        length = free_index[-1]
        free[length] -= 1
        if free[length] == 0:
            free_index.remove(length)
        if length % 2 == 0:
            increment(free, free_index, length // 2)
            increment(free, free_index, length // 2 - 1)
            max, min = length // 2, length // 2 - 1
        else:
            increment(free, free_index, length // 2)
            free[length // 2] += 1
            max, min = length // 2, length // 2

        if count == num_people:
            return max, min

        count += 1


def main():
    l = int(input())
    for i in range(l):
        max, min= occupy(input())
        print("Case #{}: {} {}".format(i + 1, max, min))

main()