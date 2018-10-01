#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 KuoE0 <kuoe0.tw@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

import copy
import itertools

step = list(itertools.product(*([[-1, 0, 1]] * 2)))
step.remove((0, 0))

def expand_grid(mine_map, border_list, empty_grid):

    global step

    if empty_grid == 0:
        return mine_map

    if empty_grid < 0:
        return None

    for pos in border_list:

        remain_empty = empty_grid
        new_map = copy.deepcopy(mine_map)
        new_border = copy.deepcopy(border_list)
        new_border.remove(pos)

        for s in step:

            next_pos = pos[0] + s[0], pos[1] + s[1]

            if next_pos[0] not in xrange(len(mine_map)) or next_pos[1] not in xrange(len(mine_map[0])):
                continue

            if new_map[next_pos[0]][next_pos[1]] == '*':
                new_map[next_pos[0]][next_pos[1]] = '.'
                remain_empty -= 1
                new_border.append(next_pos)

        ret = expand_grid(new_map, new_border, remain_empty)

        if ret:
            return ret



        



    

T = input()

for t in xrange(T):

    R, C, M = [int(x) for x in raw_input().split()]

    min_area = min(2, R) * min(2, C)

    print "Case #{0}:".format(t + 1)

    mine_map = [['*' for i in xrange(C)] for j in xrange(R)]

    mine_map[0][0] = '.'
    ret = expand_grid(mine_map, [(0,0)], R * C - M - 1)

    if ret:
        ret[0][0] = 'c'
        for line in ret:
            print ''.join(line)

    else:
        print 'Impossible'

