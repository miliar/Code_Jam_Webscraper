from __future__ import division
import sys
import math

input = open('input.in')
output = open('out', 'wb')


class gcj:
    IN = input
    number = 0

    @classmethod
    def case(cls):
        cls.number += 1
        return 'Case #%d: ' % cls.number

    @classmethod
    def line(cls, type=str):
        line = cls.IN.readline()
        return type(line.strip('\n'))

    @classmethod
    def split_line(cls, type=str):
        line = cls.IN.readline()
        # print line
        return [type(x) for x in line.split()]

def solve(N, K):
    f = math.floor(math.log(K,2))
    n_remain = N - 2**f + 1
    s = 2**f
    base = n_remain // s
    r = n_remain % s
    rank = K - s + 1
    if rank <= r:
        base += 1
    if base % 2 == 0:
        return [base//2, base//2-1]
    else:
        return [(base-1)//2, (base-1)//2]
        

def main():
    t = gcj.line(int)

    for i in xrange(t):
        N, K = gcj.split_line(int)
        ans = solve(N, K)
        output.write(gcj.case() + str(int(ans[0])) + ' ' + str(int(ans[1])) + '\n')

    input.close()
    output.close()


if __name__ == '__main__':
    main()
