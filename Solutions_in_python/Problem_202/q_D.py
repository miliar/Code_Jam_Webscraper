
# -*- coding: UTF-8 -*-

import sys


def debug(msg):
    sys.stderr.write(msg)
    sys.stderr.flush()


NONE = 0
PLUS = 1
CROSS = 2
SUPER = 3

TYPE = 0
OK_PLUS = 1
OK_CROSS = 2


#def delete_model(table, x, y):
#    previous_type = table[x][y][0]
#    table[x][y][0] = NONE

#    if previous_type == PLUS:
#    elif previous_type == CROSS:

def ban_plus(table, x, y):
    if 0 <= x < len(table) and 0 <= y < len(table):
        table[x][y][OK_PLUS] = False


def ban_cross(table, x, y):
    if 0 <= x < len(table) and 0 <= y < len(table):
        table[x][y][OK_CROSS] = False


def update_table(table, model):
    #debug("new model: " + str(model) + "\n")
    model_type = model[0]
    x = model[1]
    y = model[2]

    table[x][y][TYPE] = model_type

    # update bans information
    if model_type == CROSS or model_type == SUPER:
        for i in range(len(table)):
            if i != x:
                ban_plus(table, i, y)
            if i != y:
                ban_plus(table, x, i)

    if model_type == PLUS or model_type == SUPER:
        for i in range(len(table)):
            if i != y:
                ban_cross(table, x - y + i, i)
                ban_cross(table, x + y - i, i)

    #debug(str(table))
    #debug("\n")

def upgrade_cell(table, x, y, ans):
    #debug("upgrade:" + str(x) + "," + str(y) + "\n")
    info = table[x][y]
    new_model_type = NONE
    if info[OK_PLUS] and info[OK_CROSS] and info[TYPE] != SUPER:
        new_model_type = SUPER
    elif info[OK_CROSS] and info[TYPE] == NONE:
        new_model_type = PLUS
    elif info[OK_PLUS] and info[TYPE] == NONE:
        new_model_type = CROSS

    if new_model_type == NONE:
        return 0

    ret = 1
    if new_model_type == SUPER and table[x][y][TYPE] == NONE:
        ret = 2

    ans.append([new_model_type, x, y])
    update_table(table, [new_model_type, x, y])

    return ret

def solve(n, models):
    table = [[[NONE, True, True] for i in range(n)] for j in range(n)]

    ans_point = 0
    ans = []

    for model in models:
        update_table(table, model)
        if model[TYPE] == CROSS or model[TYPE] == PLUS:
            ans_point += 1
        elif model[TYPE] == SUPER:
            ans_point += 2


    for track in range(n/2):
        for i in range(track, n - track - 1):
            ans_point += upgrade_cell(table, track, i, ans)
        for i in range(track, n - track - 1):
            ans_point += upgrade_cell(table, i, n - track - 1, ans)
        for i in range(track, n - track - 1):
            ans_point += upgrade_cell(table, n - track - 1, n - 1 - i, ans)
        for i in range(track, n - track - 1):
            ans_point += upgrade_cell(table, n - 1 - i, track, ans)

    if n % 2 == 1:
        ans_point += upgrade_cell(table, n / 2, n / 2, ans)

    '''
    for x in range(len(table)):
        for y in range(len(table[x])):
            info = table[x][y]
            new_model_type = NONE
            if info[OK_PLUS] and info[OK_CROSS] and info[TYPE] != SUPER:
                new_model_type = SUPER
            elif info[OK_CROSS] and info[TYPE] == NONE:
                new_model_type = PLUS
            elif info[OK_PLUS] and info[TYPE] == NONE:
                new_model_type = CROSS

            if new_model_type == NONE:
                continue

            if new_model_type == SUPER and info[TYPE] == NONE:
                ans_point += 2
            else:
                ans_point += 1
            ans.append([new_model_type, x, y])
            update_table(table, [new_model_type, x, y])
    '''
    '''
    for x in range(len(table)):
        for y in range(len(table[x])):
            info = table[x][y]
            if info[OK_PLUS] and info[OK_CROSS] and info[TYPE] != SUPER:
                if info[TYPE] == NONE:
                    ans_point += 2
                else:
                    ans_point += 1
                ans.append([SUPER, x, y])
                update_table(table, [SUPER, x, y])

    for x in range(len(table)):
        for y in range(len(table[x])):
            info = table[x][y]
            if info[OK_CROSS] and info[TYPE] == NONE:
                ans_point += 1
                ans.append([PLUS, x, y])
                update_table(table, [PLUS, x, y])

    for x in range(len(table)):
        for y in range(len(table[x])):
            info = table[x][y]
            if info[OK_PLUS] and info[TYPE] == NONE:
                ans_point += 1
                ans.append([CROSS, x, y])
                update_table(table, [CROSS, x, y])
    '''
    '''
    for x in range(len(table)):
        for y in range(len(table[x])):
            info = table[x][y]
            if info[OK_CROSS] and info[TYPE] == NONE:
                ans_point += 1
                ans.append([PLUS, x, y])
                update_table(table, [PLUS, x, y])

    for x in range(len(table)):
        for y in range(len(table[x])):
            info = table[x][y]
            if info[OK_PLUS] and info[TYPE] == NONE:
                ans_point += 1
                ans.append([CROSS, x, y])
                update_table(table, [CROSS, x, y])

    for x in range(len(table)):
        for y in range(len(table[x])):
            info = table[x][y]
            if info[OK_PLUS] and info[OK_CROSS] and info[TYPE] != SUPER:
                if info[TYPE] == NONE:
                    ans_point += 2
                else:
                    ans_point += 1
                ans.append([SUPER, x, y])
                update_table(table, [SUPER, x, y])
    '''
    '''
    for x in range(len(table)):
        for y in range(len(table[x])):
            info = table[x][y]
            if info[OK_PLUS] and info[OK_CROSS] and info[TYPE] != SUPER:
                if info[TYPE] == NONE:
                    ans_point += 2
                    ans.append([SUPER, x, y])
                    update_table(table, [SUPER, x, y])

    for x in range(len(table)):
        for y in range(len(table[x])):
            info = table[x][y]
            if info[OK_PLUS] and info[OK_CROSS] and info[TYPE] != SUPER:
                if info[TYPE] != NONE:
                    ans_point += 1
                    ans.append([SUPER, x, y])
                    update_table(table, [SUPER, x, y])

    for x in range(len(table)):
        for y in range(len(table[x])):
            info = table[x][y]
            if info[OK_CROSS] and info[TYPE] == NONE:
                ans_point += 1
                ans.append([PLUS, x, y])
                update_table(table, [PLUS, x, y])

    for x in range(len(table)):
        for y in range(len(table[x])):
            info = table[x][y]
            if info[OK_PLUS] and info[TYPE] == NONE:
                ans_point += 1
                ans.append([CROSS, x, y])
                update_table(table, [CROSS, x, y])
    '''

    return [ans_point, ans]

#input_file = "sample.in"
#input_file = "D-small-attempt1.in"
input_file = "D-large.in"
f = open(input_file)
sys.stdout = open(input_file.replace(".in", ".txt"), 'w')
tc_num = int(f.readline().rstrip())

line_num = 2
for tc in range(tc_num):
    debug("Case #" + str(tc + 1) + "begin " + str(line_num) + "\n")
    l = f.readline().rstrip().split()
    line_num += 1
    n = int(l[0])
    m = int(l[1])
    models = []
    for i in range(m):
        l = f.readline().rstrip().split()
        line_num += 1
        type_char = l[0]

        if type_char == '+':
            model_type = PLUS
        elif type_char == 'x':
            model_type = CROSS
        else:
            model_type = SUPER

        models.append([model_type, int(l[1])-1, int(l[2])-1])

    ans = solve(n, models)
    print("Case #" + str(tc + 1) + ": " + str(ans[0]) + " " + str(len(ans[1])))
    for model in ans[1]:
        if model[TYPE] == PLUS:
            type_char = '+'
        elif model[TYPE] == CROSS:
            type_char = 'x'
        else:
            type_char = 'o'

        print(type_char + " " + str(model[1]+1) + " " + str(model[2]+1))

