# *-* coding:utf-8 *-*
# google code jam R1, problem B


def main_result(n, r, o, y, g, b, v):
    s = ""
    my_color = [r, o, y, g, b, v]

    for ii in [1, 3, 5]:
        if my_color[dict_possible_neighbor[ii][0]] < my_color[ii]:
            return "IMPOSSIBLE"
    for kk in [0, 2, 4]:
        if sum([my_color[ss] for ss in dict_possible_neighbor[kk]]) < my_color[kk]:
            return "IMPOSSIBLE"

    # for iii in xrange(6):
    #     if my_color[iii] == 0:
    #         my_color[iii] = -1001

    min_index = get_max_index(my_color)
    first_index = min_index
    s += dict_color_int[min_index]
    my_color[min_index] -= 1
    for j in xrange(n-1):
        poss = dict_possible_neighbor[min_index]
        temp = [0, 0, 0, 0, 0, 0]
        for po in poss:
            temp[po] = my_color[po]
        min_index = get_max_index(temp, first_index)
        if my_color[min_index] == 0:
            return "IMPOSSIBLE"
        s += dict_color_int[min_index]
        my_color[min_index] -= 1
    if s[0] == s[-1]:
        return "IMPOSSIBLE"
    return s


def get_max_index(color_arr, first=-1):
    max_c = max(color_arr)
    max_index = 0
    min_sum = 1000000
    for ij in xrange(6):
        if color_arr[ij] == max_c:
            pos = dict_possible_neighbor[ij]
            my_sum = sum([color_arr[j] for j in pos])
            if my_sum < min_sum:
                max_index = ij
                min_sum = my_sum

    for kj in xrange(6):
        if color_arr[kj] == max_c:
            pos = dict_possible_neighbor[kj]
            a_sum = sum([color_arr[k] for k in pos])
            if a_sum == min_sum:
                if kj == first:
                    return kj
    return max_index



# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
dict_possible_neighbor = [[2, 3, 4], [4], [0, 4, 5], [0], [0, 1, 2], [2]]
dict_color_int = ["R", "O", "Y", "G", "B", "V"]
for i in xrange(1, t + 1):
    n, r, o, y, g, b, v = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    # n = int(raw_input())
    result = main_result(n, r, o, y, g, b, v)
    print "Case #{}: {}".format(i, result)



