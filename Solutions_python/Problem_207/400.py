# -*- coding: utf-8 -*-
# !python3

__author__ = 'lostcoaster'

from trivial.codejam_thingy.files import Problem


class UniPony(Problem):
    def __init__(self):
        super(UniPony, self).__init__('B-small-attempt1')

    def solve(self, in_file):
        n, *c = (int(x) for x in in_file.readline().strip().split(' '))
        ori_c = c[:]
        mapping = ['R', 'O', 'Y', 'G', 'B', 'V']
        # small cases
        ret = ''
        last_color = -1
        while c[0] + c[2] + c[4] > 0:
            ch = max(zip((c[x] for x in [0, 2, 4] if x != last_color), (x for x in [0, 2, 4] if x != last_color)))
            ret += mapping[ch[1]]
            last_color = ch[1]
            c[ch[1]] -= 1
            if any(x < 0 for x in c):
                return 'IMPOSSIBLE'
        if ret[-1] != ret[0]:
            return ret
        elif ret[-3] != ret[-1]:
            ret = ret[:-2]+ret[-1]+ret[-2]
            self.validate(ret, n)
            return ret
        else:
            return 'IMPOSSIBLE'

    def validate(self, ret, n):
        assert ret[-1] != ret[0]
        last_c = None
        for c in ret:
            assert c != last_c
            last_c = c
            n -= 1
        assert n == 0




if __name__ == '__main__':
    UniPony().run()
