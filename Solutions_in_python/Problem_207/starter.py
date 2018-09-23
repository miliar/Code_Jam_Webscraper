#!/usr/bin/env python

import sys
import math

def process_input():
    with open("input.txt") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content

def print_result(global_counter, r):
    print "Case #" + str(global_counter) + ":", r

def determine():
    return True

def single_run(data, global_counter):
    (N, R, O, Y, G, B, V) = [int(x) for x in data.split(' ')]
    final_out = ''
    single_non_zero = (0 if R == 0  else 1) + (0 if Y == 0 else 1) + (0 if B == 0 else 1)
    # print "single_non_zero", single_non_zero
    double_non_zero = (0 if O == 0  else 1) + (0 if G == 0 else 1) + (0 if V == 0 else 1)
    # print "double_non_zero", double_non_zero
    while R != 0 or Y != 0 or B != 0:
        cur_largest = max(R, B)
        cur_largest = max(cur_largest, Y)
        cur_lar_c = ''
        cur_sec_lar_c = ''
        if R == cur_largest:
            cur_lar_c = 'R'
            if B >= Y:
                cur_sec_lar_c = 'B'
            else:
                cur_sec_lar_c = 'Y'
        elif B == cur_largest:
            cur_lar_c = 'B'
            if R >= Y:
                cur_sec_lar_c = 'R'
            else:
                cur_sec_lar_c = 'Y'
        elif Y == cur_largest:
            cur_lar_c = 'Y'
            if R >= B:
                cur_sec_lar_c = 'R'
            else:
                cur_sec_lar_c = 'B'
        # print "begin", R, Y, B, final_out, cur_lar_c
        if len(final_out) == 0:
            final_out += cur_lar_c
            if cur_lar_c == 'R':
                R -= 1
            if cur_lar_c == 'Y':
                Y -= 1
            if cur_lar_c == 'B':
                B -= 1
            continue
        cur_last = final_out[len(final_out) - 1]
        cur_first = final_out[0]
        if cur_last == 'R' and 'R' == cur_lar_c:
            if 'Y' == cur_sec_lar_c and Y > 0:
                final_out += 'Y'
                Y -= 1
            elif B > 0:
                final_out += 'B'
                B -= 1
            else:
                final_out = "IMPOSSIBLE"
                break
        elif cur_last == 'Y' and 'Y' == cur_lar_c:
            if B > 0 and 'B' == cur_sec_lar_c:
                final_out += 'B'
                B -= 1
            elif R > 0:
                final_out += 'R'
                R -= 1
            else:
                final_out = "IMPOSSIBLE"
                break
        elif cur_last == 'B' and 'B' == cur_lar_c:
            if R > 0 and 'R' == cur_sec_lar_c:
                final_out += 'R'
                R -= 1
            elif Y > 0:
                final_out += 'Y'
                Y -= 1
            else:
                final_out = "IMPOSSIBLE"
                break
        elif cur_last == 'R':
            if 'Y' == cur_lar_c and Y > 0:
                final_out += 'Y'
                Y -= 1
            elif B > 0:
                final_out += 'B'
                B -= 1
            else:
                final_out = "IMPOSSIBLE"
                break
        elif cur_last == 'Y':
            if B > 0 and 'B' == cur_lar_c:
                final_out += 'B'
                B -= 1
            elif R > 0:
                final_out += 'R'
                R -= 1
            else:
                final_out = "IMPOSSIBLE"
                break
        elif cur_last == 'B':
            if R > 0 and 'R' == cur_lar_c:
                final_out += 'R'
                R -= 1
            elif Y > 0:
                final_out += 'Y'
                Y -= 1
            else:
                final_out = "IMPOSSIBLE"
                break
        else:
            print "SHOULD NOT REACH HERE"
        if Y + R + B == 0:
            cur_last = final_out[len(final_out) - 1]
            cur_first = final_out[0]
            if cur_last == cur_first:
                if(len(final_out) >= 3):
                    sec_last = final_out[len(final_out) - 2]
                    last = final_out[len(final_out) - 1]
                    if final_out[len(final_out) - 3] != last:
                        # final_out[len(final_out) - 2] = last
                        final_out_lst = list(final_out)
                        final_out_lst[len(final_out) - 2] = last
                        # final_out[len(final_out) - 1] = sec_last
                        final_out_lst[len(final_out) - 1] = sec_last
                        final_out = "".join(final_out_lst)
                        break
                final_out = "IMPOSSIBLE"
        # print "end", R, Y, B, final_out
    # print final_out
    print_result(global_counter, final_out);





def main():
    content = process_input()
    data_size = int(content.pop(0))
    global_counter = 1
    for line in content:
        data = (line)
        single_run(data, global_counter)
        global_counter += 1

main()
