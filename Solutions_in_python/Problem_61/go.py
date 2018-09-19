import copy
import sys
from pprint import pprint
from copy import deepcopy

input = file(sys.argv[1])
count = int(input.readline())
i = 1

def permute(a_list):
    if len(a_list) == 1:
        yield a_list
    else:
        for permutation in permute(a_list[1:]):
            x = [a_list[0]] + permutation
            y = permutation
            try:
                permutation.index(a_list[-1])
            except:
                break
            yield x
            yield y

def pure(a_list, num):
    visited = []
    try:
        index = a_list.index(num) + 1
    except:
        return False
    while index != 1:
        if index in visited:
            return False
        else:
            visited.append(index)
        try:
            index = a_list.index(index) + 1
        except:
            return False
    return True

results = {}
while i <= count:
    if i == 30:
        import pdb;pdb.set_trace()
    magic = int(input.readline())
    a_list = range(2, magic+1)
    result = 0
    if magic not in results.keys():
        for list in permute(a_list):
            if pure(list, magic):
                result += 1
    else:
        result = results[magic]
    result = result % 100003
    results[magic] = result
    print 'Case #%i: %i' % (i, result)
    i += 1
