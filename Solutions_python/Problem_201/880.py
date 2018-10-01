t = int(raw_input())
for i in xrange(1, t + 1):
    stalls, people = raw_input().split(" ")
    stalls = int(stalls)
    people = int(people)

    while people:
        if stalls % 2:
            max = stalls / 2
            min = max
        else:
            max = stalls / 2
            min = max - 1

        if people % 2:
            stalls = min
        else:
            stalls = max

        people = people / 2

    print "Case #{}: {} {}".format(i, max, min)

    # stalls_list = ["x"]
    # for x in xrange(0, stalls):
    #     stalls_list.append("o")
    # stalls_list.append("x")
    #
    # # if len(stalls_list) % 2:
    # #     stalls_list[len(stalls_list) / 2] = "x"
    # # else:
    # #     stalls_list[len(stalls_list) / 2 - 1] = "x"
    #
    # stalls_info = {}
    #
    # if stalls == people:
    #     a_1 = 0
    #     a_2 = 0
    # elif people == 1:
    #     if len(stalls_list) % 2:
    #         index = len(stalls_list) / 2
    #         a_1 = index - 1
    #         a_2 = index - 1
    #     else:
    #         index = len(stalls_list) / 2 - 1
    #         a_1 = index
    #         a_2 = index - 1
    # elif stalls == people + 1:
    #     a_1 = 0
    #     a_2 = 0
    # elif stalls / 2 == people + 1:
    #     a_1 = 1
    #     a_2 = 0
    # else:
    #     for person in range(0, people):
    #         for stall_index, stall_info in enumerate(stalls_list):
    #             if stall_info == "o":
    #                 l = stall_index - (''.join(stalls_list[:stall_index]).rfind('x') + 1)
    #                 r = ''.join(stalls_list[stall_index:]).find('x') - 1
    #                 stalls_info[stall_index] = [l, r]
    #             else:
    #                 stalls_info[stall_index] = [0, 0]
    #
    #         max_min_stalls = 0
    #         _max_min_stalls = 0
    #         first = True
    #         for stall_index, stall_info in stalls_info.iteritems():
    #             if min(stall_info) > max_min_stalls:
    #                 max_min_stalls = min(stall_info)
    #                 _max_min_stalls = max(stall_info)
    #                 max_stalls_index = stall_index
    #             elif min(stall_info) == max_min_stalls:
    #                 if max(stall_info) > _max_min_stalls:
    #                     max_min_stalls = min(stall_info)
    #                     _max_min_stalls = max(stall_info)
    #                     max_stalls_index = stall_index
    #
    #         stalls_list[max_stalls_index] = "x"
    #
    #     a_1 = max(stalls_info[max_stalls_index])
    #     a_2 = min(stalls_info[max_stalls_index])
    #
    # print "Case #{}: {} {}".format(i, a_1, a_2)