# -*- coding: utf-8 -*-

def solve(n):
    ret = [int(e) for e in str(n)]
    for k in range(20):
        for i in range(len(ret) - 1):
            if ret[i] > ret[i + 1]:
                ret[i] -= 1
                for j in range(i + 1, len(ret)):
                    ret[j] = 9

    return int(''.join([str(e) for e in ret]))


def main():
    t = int(input())
    for i in range(1, t + 1):
        n = int(input())
        print('Case #%d: %d' % (i, solve(n)))


if __name__ == '__main__':
    main()
