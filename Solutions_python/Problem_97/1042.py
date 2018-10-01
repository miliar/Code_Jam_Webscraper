import sys
import itertools


def is_recycled(x, y):
    if x == y:
        return False

    x = str(x)
    y = str(y)

    if len(x) != len(y):
        return False

    for char in x:
        x = x[-1] + x[:-1]

        if x[0] == '0':
            continue

        if x == y:
            return True

    return False


def check_pair(min_num, max_num):
    mid_point = ((max_num - min_num) / 2) + min_num

    recycled_count = 0

    unique_pairs = set()

    for x in itertools.count(min_num, 1):
        for y in itertools.count(max_num, -1):
            if x >= y:
                break

            if is_recycled(x, y):
                unique_pairs.add((min(x, y),max(x, y)))

        if x > max_num:
            break

    unique_pairs = list(unique_pairs)
    unique_pairs.sort(key=lambda x: x[0])

    #for pair in unique_pairs:
    #    print '%d is recycled of %d' % pair

    return len(unique_pairs)

if __name__ == '__main__':
    with open(sys.argv[1]) as fd:
        fd.readline()

        for idx, line in enumerate(fd):
            print 'Case #%d: %d' % (idx + 1, check_pair(*[int(x) for x in line.split(' ')]))
