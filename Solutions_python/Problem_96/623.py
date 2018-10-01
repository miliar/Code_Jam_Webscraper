#!/usr/bin/env python
#
# Google Code Jam 2012
# Nathan Williams <nlwsother@gmail.com>
# Qualification Round, Problem B, Dancing With the Googlers
#

import sys

DEBUG = False
ERROR = True
OUTPUT = True
RUN_TEST_CASE = True

def log(do_log, s):
    if do_log:
        print str(s)


OUT_NORMAL = 0
OUT_SURPRISING = 1
OUT_LOOKED_AT = 2

def all_results(max_score):
    log(DEBUG, "total_score: %s" % max_score)
    output = [None, None, 0]
    for i in range(0,11):# range(max(max_score/3-1,0), min(max_score/3+2,11,max_score)):
        for j in range(0,11): #range(i, min(i+3,11)): #range(max(i-2,0), min(i+3,11)):
            for k in range(0,11):#range(j, min(i+3,j+3,11)): #range(max(max(j-2, i-2), 0), min(min(i+3, j+3), 11)):
                output[OUT_LOOKED_AT] += 1

                if (i + j + k) == max_score:
                    tup = (i,j,k)
                    log(DEBUG, tup)
                    diff = max(tup) - min(tup)
                    if diff > 2:
                        log(DEBUG, 'WRONG')
                    elif diff == 2:
                        output[OUT_SURPRISING] = tup
                    else:
                        output[OUT_NORMAL] = tup

                    if output[OUT_NORMAL] != None and output[OUT_SURPRISING] != None:
                        return output
    return output


def count_possible(num_googler, num_surprising, best_result, point_tuple):
    log(DEBUG, "num=%d sur=%d best=%d" % (num_googler, num_surprising, best_result))
    if num_googler != len(point_tuple):
        log(DEBUG, "BAD INPUT point_tuple")
        return -1

    all_outputs = []
    for pt in point_tuple:
        cur_out = all_results(pt)
        all_outputs.append(cur_out)

    count_normal = 0
    count_surprising = 0
    for out in all_outputs:
        norm = out[OUT_NORMAL]
        sur = out[OUT_SURPRISING]
        if norm and max(norm) >= best_result:
            count_normal += 1
        elif sur and max(sur) >= best_result:
            count_surprising += 1

    total = count_normal + min(count_surprising, num_surprising)
    log(DEBUG, "norm=%d sur=%d final=%d" % (count_normal, count_surprising, total))
    return total


if RUN_TEST_CASE:
    if count_possible(3, 1, 5, (15,13,11)) != 3:
        log(ERROR, "TEST1 FAILED")
    if count_possible(3, 0, 8, (23,22,21)) != 2: 
        log(ERROR, "TEST2 FAILED")
    if count_possible(2, 1, 1, (8,0)) != 1:
        log(ERROR, "TEST3 FAILED")
    if count_possible(6, 2, 8, (29,20,8,18,18,21)) != 3:
        log(ERROR, "TEST4 FAILED")


if len(sys.argv) == 1:
    sys.exit(0)
elif len(sys.argv) > 2:
    log(DEBUG, "Too many command line arguments")


log(DEBUG, "Processing %s\n" % sys.argv[1])

read_count = False
read_lines = 0
input_file = open(sys.argv[1])

for cur_line in input_file:
    if read_count is False:
        read_count = int(cur_line)
    elif read_lines == read_count:
        break
    else:
        read_lines += 1
        # Spec: no spaces at begin or end of line
        split_text = cur_line.strip().split(' ')
        if len(split_text) < 3 or len(split_text) != (int(split_text[0]) + 3):
            log(ERROR, "Malformed split_text: %s" % str(split_text))
        else:
            googlers = int(split_text[0])
            surprising = int(split_text[1])
            best_result = int(split_text[2])
            total_scores = []
            for i in range(3, len(split_text)):
                total_scores.append(int(split_text[i]))
            max_having_best = count_possible(googlers, surprising, best_result, total_scores)
            log(OUTPUT, 'Case #%d: %d' % (read_lines, max_having_best))

input_file.close()
