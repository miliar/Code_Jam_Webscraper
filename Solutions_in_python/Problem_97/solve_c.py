#!/bin/python
import sys
from multiprocessing import Process, Queue
from datetime import datetime

def get_a_b(line):
    items = line[:-1].split(' ')
    items = [int(i) for i in items]
    return items[0], items[1]

def create_rotate_nums(num, max):
    result_list = []
    str_num = str(num)
    for i in range(0, len(str_num)):
        num_rotated = int(str_num[i:] + str_num[:i]);
        if num_rotated > num and num_rotated <= max:
            result_list.append(num_rotated)
    return list(set(result_list))

def solve(a, b):
    result = 0
    for n in range(a, b+1):
        rlist = create_rotate_nums(n, b)
        result += len(rlist)
    return result

def main(file):
    outfile = file.replace('in', 'out')

    i_testcase = 0
    q = Queue()
    process_list = []
    for line in open(file, 'r'):
        if i_testcase:
            a, b = get_a_b(line)
            # p = Process(target=solve, args=(i_testcase,a,b,))
            # p.start()
            # process_list.append(p)
            #result = solve(a, b)
            result = solve(a, b)
            print 'Case #%d: %d\n' % (i_testcase, result)
            # SAVE
            f = open(outfile, 'a')
            f.write('Case #%d: %d\n' % (i_testcase, result))
            f.close()
        i_testcase += 1

    # map(lambda p: p.join(), process_list)
    # for q

if __name__ == '__main__':
    start = datetime.now()
    main(sys.argv[1])
    end = datetime.now()
    print end - start
