#!env python2

from collections import Counter
import sys


failed_combinations = set()


def get_chest_order(keys, chests, indices):
    for offset, (index, key_needed, keys_given) in enumerate(chests):
        if keys[key_needed] > 0:
            next_indices = indices + [index]
            chests_selected = tuple(sorted(next_indices))

            if chests_selected in failed_combinations:
                continue

            next_keys = keys + Counter(keys_given) - Counter([key_needed])

            if len(chests) == 1:
                return next_indices

            next_chests = list(chests)
            next_chests.pop(offset)

            following_chests = get_chest_order(
                next_keys, next_chests, next_indices)

            if following_chests is None:
                failed_combinations.add(chests_selected)
            if following_chests is not None:
                return following_chests

    return None


def read_ints(line):
    return map(int, line.strip().split(' '))


def read_input():
    count = int(sys.stdin.readline().strip())

    for _ in range(count):
        num_keys, num_chests = read_ints(sys.stdin.readline())
        keys = read_ints(sys.stdin.readline())
        chests = []

        for _ in range(num_chests):
            chest_desc = read_ints(sys.stdin.readline())
            key_needed = chest_desc[0]
            keys_given = chest_desc[2:]
            chests.append((key_needed, keys_given))

        yield keys, chests


case = 1
for keys, chests in read_input():
    failed_combinations.clear()
    enumerated_chests = [(i, k, g) for i, (k, g) in enumerate(chests)]
    chest_order = get_chest_order(Counter(keys), enumerated_chests, [])

    if chest_order is None:
        result = 'IMPOSSIBLE'
    else:
        result = ' '.join([str(k + 1) for k in chest_order])

    print "Case #%d: %s" % (case, result)
    case += 1
