'''
Created on 2010/05/08
@author: aflc
'''
import sys

def calc(R, k, groups):
    res = 0
    for i in range(R):
        rider = []
        cnt = 0
        while groups:
            if cnt + groups[0] > k:
                break
            else:
                one = groups.pop(0)
                cnt += one
                rider.append(one)

        res += cnt
        groups += rider

    return res


with open('out.txt', 'w') as fo:
    num = 0
    count = -1
    R, k, groups = None, None, []
    for line in open(sys.argv[1], 'r'):
        count += 1
        if count == 1:
            R, k, N = map(int, line.strip().split(' '))
        elif count == 2:
            groups = list(map(int, line.strip().split(' ')))
            count = 0
            num += 1
            #
            res = calc(R, k, groups)
            fo.write('Case #' + str(num) + ': ' + str(res) + '\n')
            #
