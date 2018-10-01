#!/usr/bin/env python
# -*- coding: utf-8  -*-

import sys
import os

input_path = sys.argv[1]
output_path = sys.argv[2]

def do_algorithm(test_idx, input_file, output_file):
    num_dic = dict()
    # First Selection
    row_selected = int(input_file.readline())
    for i in range(4):
        line = input_file.readline()
        cur_row = i + 1
        if cur_row != row_selected:
            continue
        arr = line.split()
        for item in arr:
            num_dic[item] = 1

    # Second Selection
    row_selected = int(input_file.readline())
    for i in range(4):
        line = input_file.readline()
        cur_row = i + 1
        if cur_row != row_selected:
            continue
        arr = line.split()
        for item in arr:
            if item in num_dic:
                num_dic[item] = num_dic[item] + 1
            else:
                num_dic[item] = 1
   
    # Scan dic
    multi_choosen_cnt = 0
    last_item = -1
    for item in num_dic:
        value = num_dic[item]
        if value == 2:
            multi_choosen_cnt = multi_choosen_cnt + 1
            last_item = item

    # Answer
    if multi_choosen_cnt == 0:
        output_file.write('Case #%d: Volunteer cheated!\n' % test_idx)
    elif multi_choosen_cnt == 1:
        output_file.write('Case #%d: %d\n' % (test_idx, int(last_item)))
    else:
        output_file.write('Case #%d: Bad magician!\n' % test_idx)

try:
    input_file = open(input_path, 'r')
    output_file = open(output_path, 'w')

    test_num = int(input_file.readline())
    for i in range(test_num):
        do_algorithm(i+1, input_file, output_file)

    input_file.close()
    output_file.close()
except Exception as e:
    print str(e)
    sys.exit(-1)


