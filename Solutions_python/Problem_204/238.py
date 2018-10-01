#!/usr/bin/env python3
import math
import sys
from typing import List, Tuple, Union


class BreakLoop(Exception):
    pass


class Range:
    def __init__(self, from_: int, to: int):
        self.from_ = from_
        self.to = to

    def __contains__(self, item: int):
        return self.from_ <= item < self.to

    def __repr__(self):
        return 'Range(%r, %r)' % (self.from_, self.to)

    def __bool__(self):
        return self.from_ < self.to

    def __iter__(self):
        for i in range(self.from_, self.to):
            yield i

    def torange(self):
        return range(self.from_, self.to)

    def intersect(self, from_: int, to: int):
        if self.from_ < from_:
            self.from_ = from_
        if self.to > to:
            self.to = to
        return self


def debug(s):
    print(s, file=sys.stderr)


def get_range(value: Union[int, float], minimum: Union[int, float], maximum: Union[int, float]):
    return Range(int(math.ceil(value / maximum) + 0.000001), int(value / minimum) + 1)


for case_num in range(int(input())):
    debug('case number: %r' % (case_num + 1,))
    num_ingredients, num_packages = (int(i) for i in input().split())
    ing_ranges: List[Tuple[int, int]] = [(int(i) * 0.9, int(i) * 1.1) for i in input().split()]
    quantities: List[List[int]] = [sorted(int(i) for i in input().split()) for _ in range(num_ingredients)]
    counters = [0] * num_ingredients
    total = 0
    try:
        while max(counters) < num_packages:
            possible_num_servings = get_range(quantities[0][counters[0]], *ing_ranges[0])
            if not possible_num_servings:
                counters[0] += 1
                continue
            # for each ingredient after the first one...
            for ing_num in range(1, num_ingredients):
                # find the first suitable quantity:
                q = quantities[ing_num]
                for i in range(counters[ing_num], num_packages):
                    intersection = get_range(q[i], *ing_ranges[ing_num]).intersect(possible_num_servings.from_,
                                                                                   possible_num_servings.to)
                    if intersection:
                        possible_num_servings = intersection
                        break
                else:
                    counters[0] += 1
                    break
                # and set it in counters
                counters[ing_num] = i
            else:
                total += 1
                for i in range(num_ingredients):
                    counters[i] += 1
    except BreakLoop:
        pass
    print('Case #%d: %d' % (case_num + 1, total))


if __name__ == '__main__':
    sum([0])
