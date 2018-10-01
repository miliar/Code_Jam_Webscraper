#!/usr/bin/python
# coding: UTF-8


def Ken_st(ken_block_left, told_naomi):
    if told_naomi > max(ken_block_left):
        return min(ken_block_left)
    else:
        return dif_min(ken_block_left, told_naomi)


def list_to_float(list_from):
    for i in range(len(list_from)):
        list_from[i] = float(list_from[i])
    return list_from


def naomi_st(naomi_block_left, ken_block_left):
    point = 0
    for block in naomi_block_left:
        chosen_ken = Ken_st(ken_block_left, block)
        # print ken_block_left
        # print str(block) + ' ' + str(chosen_ken)
        if block > chosen_ken:
            point += 1
        ken_block_left.remove(chosen_ken)
    return point


def naomi_deceitful_st(naomi_block_left, ken_block_left):
    point = 0
    for i in range(len(naomi_block_left)):
        # you actually don't need this if?
        if min(naomi_block_left) < min(ken_block_left):
            told_naomi = max(ken_block_left) - 0.000001
            chosen_ken = Ken_st(ken_block_left, told_naomi)
            chosen_naomi = min(naomi_block_left)
            if chosen_naomi > chosen_ken:
                point += 1
            ken_block_left.remove(chosen_ken)
            naomi_block_left.remove(chosen_naomi)
        elif has_min(naomi_block_left, min(ken_block_left)):
        # if has_min(naomi_block_left, min(ken_block_left)):
            told_naomi = max(ken_block_left) + 0.000001
            chosen_ken = Ken_st(ken_block_left, told_naomi)
            chosen_naomi = dif_min(naomi_block_left, min(ken_block_left))
            if chosen_naomi > chosen_ken:
                point += 1
            ken_block_left.remove(chosen_ken)
            naomi_block_left.remove(chosen_naomi)
        else:
            return point
        # print naomi_block_left
        # print chosen_naomi
        # print ken_block_left
        # print chosen_ken
    return point


def has_min(list_check, min):
    for x in list_check:
        if x > min:
            return True
    return False


def dif_min(list_check, check):
    min_dif = 10
    for block in list_check:
        dif = block - check
        if dif > 0 and min_dif > dif:
            min_dif = dif
            chosen = block
    return chosen

# txtfile = open('D-small-attempt0.in').read()
txtfile = open('D-large.in').read()
# txtfile = open('test_d.txt').read()
cases = txtfile.split('\n')

case_num = int(cases[0])

# obj = open("d_small_ans.txt", "w")
obj = open("d_large_ans.txt", "w")

for a in range(case_num):
    naomi_block_left = cases[2 + a*3].split()
    ken_block_left = cases[3 + a*3].split()
    naomi_block_left = list_to_float(naomi_block_left)
    ken_block_left = list_to_float(ken_block_left)
    st = naomi_st(naomi_block_left, ken_block_left)
    ken_block_left = cases[3 + a*3].split()
    ken_block_left = list_to_float(ken_block_left)
    dst = naomi_deceitful_st(naomi_block_left, ken_block_left)
    # print 'Case #'+str(a+1)+': '+str(dst)+' '+str(st)
    print >> obj, 'Case #'+str(a+1)+': '+str(dst)+' '+str(st)
