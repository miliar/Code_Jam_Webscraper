# -*- coding: utf-8 -*-

import sys
import os

input_text_path = __file__.replace('.py', '.txt')
fd = os.open(input_text_path, os.O_RDONLY)
os.dup2(fd, sys.stdin.fileno())


T = int(input())
f = open('submit.txt', 'w')
for t in range(T):

    R, C = map(int, input().split())

    # データ
    M = []
    for r in range(R):
        row = list(input())
        M.append(row)
    #print(M)

    # 関数定義
    # アルファベットを探す
    def first_char(row):
        for c in row:
            if c == '?':
                pass
            else:
                return c
        return '?'

    def expand_row(row):
        if row.count('?') == len(row):
            return row
        else:
            # 塗る文字を決定する
            fill_char = first_char(row)
            for i, c in enumerate(row):
                if c == '?':
                    row[i] = fill_char
                else:
                    fill_char = c
        return row

    # 解きます
    # よこ伸ばし 各行を見ていく
    for r in range(R):
        row = M[r]
        M[r] = expand_row(row)

    # 全部？だった行のために、たて伸ばし
    for c in range(C):
        column = []
        for row in M:
            column.append(row[c])
        expanded_column = expand_row(column)

        for r in range(R):
            M[r][c] = expanded_column[r]
    #print(M)

    # 解答をprint
    s = 'Case #{}:\n'.format(t+1)
    f.write(s)

    for row in M:
        s = ''.join(row)
        #print(s)
        f.write(s+'\n')
f.close()

