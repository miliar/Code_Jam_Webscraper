#!/usr/bin/python3.6

from itertools import count
from functools import partial


def next_line_to_ints(lines):
    return map(int, next(lines).split(' '))

f_in = open('b.in')
f_out = open('b.out', 'w')

lines = (i for i in f_in.read().splitlines())
t = int(next(lines))
fprint = partial(print, file=f_out)
# fprint = partial(print)

for case, line in enumerate(lines):
    nums = [int(n) for n in line]
    while not sorted(nums) == nums:
        for i, n in enumerate(nums[1:]):
            if n < nums[i]:
                nums[i] -= 1
                # print(nums)
                # print(nums[:i+1])
                # print(([9] * (len(nums) - i - 1)))
                nums = nums[:i+1] + ([9] * (len(nums) - i - 1))
                break


    nums = [str(n) for n in nums]
    n = int(''.join(nums))
    fprint(f'Case #{case + 1}: {n}')
