#!/usr/bin/env python
import sys

def main(o_arr, b_arr, inputs):
    results = []
    for input in xrange(0, inputs):
        time = 0
        rank = 1
        curr_o = 1
        o_arr_size = 0
        if len(o_arr[input]) > 0:
            o_arr_size = len(o_arr[input])
        curr_b = 1
        arr_index_o = 0
        arr_index_b = 0
        b_arr_size = 0
        flag = 0
        if len(b_arr[input]) > 0:
            b_arr_size = len(b_arr[input])
        while (arr_index_o < o_arr_size) or (arr_index_b < b_arr_size):
            try:
                if curr_o == o_arr[input][arr_index_o]:
                    if rank == o_arr[input][arr_index_o+1]:
                        arr_index_o += 2
                        flag = 1
                else:
                    if curr_o < o_arr[input][arr_index_o]:
                        curr_o += 1
                    else:
                        curr_o -= 1
            except IndexError:
                pass
            try:
                if curr_b == b_arr[input][arr_index_b]:
                    if rank == b_arr[input][arr_index_b+1]:
                        arr_index_b += 2
                        flag = 1
                else:
                    if curr_b < b_arr[input][arr_index_b]:
                        curr_b += 1
                    else:
                        curr_b -= 1
            except IndexError:
                pass
            if flag == 1:
                rank += 1
                flag = 0
            time += 1
            
        results.append(time)
    return results


if __name__ == "__main__":
    o_arr = []
    b_arr = []
    infile = open('A-large.in', 'rU')
    outfile = open('out', 'w')
    inputs = int(infile.readline())
    for i in xrange(0,inputs):
        input = infile.readline().split()
        o_arr.append([])
        b_arr.append([])
        rank = 1
        for r in xrange(1,(int(input[0])*2 + 1), 2):
            if input[r] == 'O':
                o_arr[i].append(int(input[r+1]))
                o_arr[i].append(rank)
                rank += 1
            else:
                b_arr[i].append(int(input[r+1]))
                b_arr[i].append(rank)
                rank += 1
    infile.close()
    results = main(o_arr, b_arr, inputs)
    for result in xrange(0, inputs):
        outfile.write(("Case #%d: %d\n") % (result+1, results[result]))
    outfile.close()
