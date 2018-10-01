#!/usr/bin/env python2

# Google Code Jam 2011 - Problem C. Candy Splitting
# David Jennings <dtkjennings@gmail.com>

import sys
import itertools

def main():
    data = sys.stdin.readlines()
    index = 1

    # loop through lines to read test cases
    for i in range(int(data[0])):
        count = int(data[index].strip())
        index += 1
        values = data[index].strip()
        index += 1
        completeTestCase(i + 1, count, values)

# count not used
def completeTestCase(case, count, values):
    test_list = [int(a) for a in values.split()]

    sum_list = { }
    sum_list['pile1_reg'] = []
    sum_list['pile1_xor'] = []
    sum_list['pile2_reg'] = []
    sum_list['pile2_xor'] = []

    for a in range(1, len(test_list)):
        comb = itertools.combinations(test_list, a)

        for c in comb:
            remaining = getRemaining(test_list, c)
            sum_list['pile1_reg'].append(sum(c))
            sum_list['pile1_xor'].append(xorSum(c))
            sum_list['pile2_reg'].append(sum(remaining))
            sum_list['pile2_xor'].append(xorSum(remaining))

    sean_largest = -1;

    # compare lists
    for x in range(len(sum_list['pile1_reg'])):
        if (sum_list['pile1_xor'][x] == sum_list['pile2_xor'][x]):
            if sum_list['pile1_reg'][x] > sean_largest:
                sean_largest = sum_list['pile1_reg'][x]

    print_value = 'NO'

    if sean_largest > 0:
        print_value = sean_largest

    print 'Case #' + str(case) + ':', print_value


def xorSum(list):
    xor_sum = 0
    for a in list:
            xor_sum ^= a
    return xor_sum

# return list of elements in the source_list not existing in comb_list
def getRemaining(source_list, comb_list):
    new_list = source_list[:]
    for a in comb_list:
        new_list.remove(a)

    return new_list


if __name__ == '__main__':
    main()
