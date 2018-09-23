def increment_by_value(d, l, index, value):
    if index in d:
        d[index] += value
    else:
        d[index] = value
        l.append(index)
        l.sort()


def occupy(s):
    num_stalls, num_people = [int(x) for x in s.split(" ")]
    free, free_index = dict(), []
    free[num_stalls] = 1
    free_index.append(num_stalls)

    count = 0
    while 1:
        #print("free ", free)
        #print("free index ", free_index)
        length = free_index[-1]

        num_served = free[length]
        free[length] = 0
        free_index.remove(length)

        #print("serving ", num_served, " people")
        if length % 2 == 0:
            increment_by_value(free, free_index, length // 2, num_served)
            increment_by_value(free, free_index, length // 2 - 1, num_served)
            max, min = length // 2, length // 2 - 1
        else:
            increment_by_value(free, free_index, length // 2, num_served * 2)
            #free[length // 2] += 1
            max, min = length // 2, length // 2

        count += num_served

        if count >= num_people:
            return max, min


def main():
    l = int(input())
    for i in range(l):
        max, min= occupy(input())
        print("Case #{}: {} {}".format(i + 1, max, min))

main()