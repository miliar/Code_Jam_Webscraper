__author__ = 'deniskrut'

import sys

t = int(sys.stdin.readline())

def countIns(cur, target):
    count = 0
    cur_sum = cur
    while cur_sum <= target:
        cur_sum = (cur_sum - 1) * 2 + 1
        count += 1
    return count, cur_sum

for o in range(0, t):
    a, n = [int (x) for x in sys.stdin.readline().split()]
    el = [int(x) for x in sys.stdin.readline().split()]
    if a == 1:
        print "Case #" + str(o + 1) + ": " + str(n)
        continue
    el.sort()
    ins = []
    ins_total_count = 0
    cur_sum = a
    for i in range(0, len(el)):
        cur_el = el[i]
        cur_ins_count, cur_value = countIns(cur_sum, cur_el)
        cur_sum = cur_value + cur_el
        ins_total_count += cur_ins_count
        ins.append(cur_ins_count)
    cur_count = ins_total_count
    res_count = ins_total_count
    for i in range(len(ins) - 1, -1, -1):
        rem = len(ins) - i
        cur_count -= ins[i]
        res_count = min(res_count, cur_count + rem)
    print "Case #" + str(o + 1) + ": " + str(res_count)