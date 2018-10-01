#!/usr/bin/env python

recipe = []
packages = []

def compose(i, left, kits, max_count):
    if i == len(packages[0]) - 1:
        kit = [packages[0][i], packages[1][left[0]]]
        kits.append(kit)
        cnt = count(kits)
        kits.remove(kit)
        if cnt > max_count:
            return cnt
        else:
            return max_count

    newleft = list(left)
    for use in xrange(len(left)):
        kit = [packages[0][i], packages[1][left[use]]]
        kits.append(kit)
        newleft.remove(left[use])
        cnt = compose(i+1, newleft, kits, max_count)
        if cnt > max_count:
            max_count = cnt
        kits.remove(kit)
        newleft.append(left[use])
    return max_count

def count(kits):
    valid = filter(lambda kit: check(kit), kits)
    return len(valid)

def check(kit):
    range_begin = 0
    range_end = 10000000
    for i in xrange(len(recipe)):
        count_begin = int(kit[i] / (recipe[i] * 1.1)) + 1
        count_end = int(kit[i] / (recipe[i] * 0.9))
        while count_begin * recipe[i] * 1.1 >= kit[i]:
            count_begin -= 1
        while count_end * recipe[i] * 0.9 <= kit[i]:
            count_end += 1

        count_begin += 1
        count_end -= 1

        if count_begin > range_begin:
            range_begin = count_begin
        if count_end < range_end:
            range_end = count_end

        if range_end < range_begin:
            return False
    return True


# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
T = int(raw_input())  # read a line with a single integer
for t in xrange(1, T + 1):
    N, P = map(lambda x: int(x), raw_input().split(" "))
    recipe = map(lambda x: int(x), raw_input().split(" "))

    packages = []
    for x in xrange(N):
        line = map(lambda x: int(x), raw_input().split(" "))
        packages.append(line)

    max_count = 0
    if N == 1:
        kits = []
        for p in packages[0]:
            kits.append([p])
        max_count = count(kits)
    else:
        max_count = compose(0, xrange(P), [], max_count)

    print "Case #{}: {}".format(t, max_count)
