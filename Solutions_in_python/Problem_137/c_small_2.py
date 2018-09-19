#!/usr/bin/python
# coding: UTF-8


def check_mine_and_draw(R, C, M):
    free_space = R * C - M
    min_space = 4
    extra_R = 0
    extra_C = 0
    if free_space == 1:
        return draw_mine(R, C, extra_C, free_space)
    if R == 1 or C == 1:
        if free_space >= 2:
            return draw_mine(R, C, extra_C, free_space)
        else:
            return "Impossible"
    else:
        for i in range(max(R, C)*2):
            # print "it " + str(i) + " extra_R " + str(extra_R) + " extra_C " + str(extra_C)
            min_space = 4 + extra_R * 2 + extra_C * 2
            # print min_space
            if free_space < min_space:
                return "Impossible"
            max_space = (2 + extra_R) * (2 + extra_C)
            # print max_space
            if min_space <= free_space <= max_space:
                return draw_mine(R, C, extra_C, free_space)
            if i % 2 == 0:
                if 2 + extra_C < C:
                    extra_C += 1
            else:
                if 2 + extra_R < R:
                    extra_R += 1


def draw_mine(R, C, extra_C, free_space):
    pict = ""
    draw = 0
    if R == 1:
        drawable = free_space
    elif C == 1:
        drawable = 1
    else:
        drawable = 2 + extra_C
    for r in range(R):
        if free_space - drawable > 0:
            if C != 1 and free_space - drawable == 1:
                draw = drawable - 1
            else:
                draw = drawable
            free_space -= draw
        else:
            draw = free_space
            free_space = 0
        pict += "."*draw + "*"*(C-draw) + "\n"
    return "c" + pict[1:len(pict)-1]

# print check_mine_and_draw(5, 1, 4)

# txtfile = open('C-small-attempt2.in').read()
txtfile = open('C-large.in').read()
# txtfile = open('test_c.txt').read()
cases = txtfile.split('\n')

case_num = int(cases[0])

obj = open("c_large_ans.out", "w")

for a in range(case_num):
    inputs = cases[a+1].split()
    R = int(inputs[0])
    C = int(inputs[1])
    M = int(inputs[2])
    # print 'Case #'+str(a+1)+':\n'+check_mine_and_draw(R, C, M)
    print >> obj, 'Case #'+str(a+1)+':\n'+check_mine_and_draw(R, C, M)
