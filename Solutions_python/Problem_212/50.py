#!/usr/bin/python

def solve(group_c, packet_size, group_sizes):
    group_dict = {}
    group_dict[0] = []
    for group_size in group_sizes:
        if group_size % packet_size == 0:
            group_dict[0].append(group_size)
    for item in group_dict[0]:
        group_sizes.remove(item)
    if 2 < packet_size:
        group_dict[2] = []
        for group_size in group_sizes:
            if group_size % packet_size == 2:
                group_dict[2].append(group_size)
        for item in group_dict[2]:
            group_sizes.remove(item)
    if 1 < packet_size:
        group_dict[1] = []
        for group_size in group_sizes:
            if group_size % packet_size == 1:
                group_dict[1].append(group_size)
        for item in group_dict[1]:
            group_sizes.remove(item)
    if 3 < packet_size:
        group_dict[3] = []
        for group_size in group_sizes:
            if group_size % packet_size == 3:
                group_dict[3].append(group_size)
        for item in group_dict[3]:
            group_sizes.remove(item)
    result = 0
    result += len(group_dict[0])
    if packet_size == 2:
        result += len(group_dict[1]) / 2
        if len(group_dict[1]) % 2 == 1:
            result += 1
    elif packet_size == 3:
        size_diff = abs(len(group_dict[1]) - len(group_dict[2]))
        common_size = min(len(group_dict[1]), len(group_dict[2]))
        result += common_size
        result += size_diff / 3
        if size_diff % 3 != 0:
            result += 1
    elif packet_size == 4:
        two_left = False
        if len(group_dict[2]) % 2 != 0:
            two_left = True
        result += len(group_dict[2]) / 2

        size_diff = abs(len(group_dict[1]) - len(group_dict[3]))
        common_size = min(len(group_dict[1]), len(group_dict[3]))
        result += common_size

        if two_left and size_diff >= 2:
            two_left = False
            size_diff -= 2
            result += 1

        result += size_diff / 4
        if size_diff % 4 != 0 or two_left:
            result += 1

    return result

import sys
input_lines = open(sys.argv[1], "rt").readlines()
stripped_input_lines = [line.strip() for line in input_lines]
num_tests = int(input_lines[0])
#print num_tests

i=1
current_line = 1
while len(stripped_input_lines) > current_line:
    #print "new test!!!!!!!!!!!"
    test_line = stripped_input_lines[current_line]
    #print test_line
    group_c = int(test_line.split()[0])
    packet_size = int(test_line.split()[1])
    current_line += 1
    current_test_line = 0
    group_sizes = []
    while current_test_line < 1:
        test_line = stripped_input_lines[current_line + current_test_line]
        group_sizes = test_line.split()
        group_sizes = [int(size) for size in group_sizes]
        current_test_line += 1
        #print test_line
    current_line += 1
    result = solve(group_c, packet_size, group_sizes)
    print "Case #"+str(i)+": "+str(result)
    i+=1
