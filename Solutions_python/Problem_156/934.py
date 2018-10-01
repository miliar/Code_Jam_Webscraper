import sys
from collections import deque



def make_it_special(current_pancakes, max_pancake):
    if max_pancake is 1:
        return

    divided = max_pancake / 2
    copies = []
    for x in range(1, divided + 1):
        copy = list(current_pancakes)
        copy.remove(max_pancake)
        copy.append(x)
        copy.append(max_pancake - x)
        copies.append(copy)
    return copies


def eat_it(current_pancakes):
    copy = [x - 1 for x in current_pancakes]
    return copy


def solve(D, Pi):
    non_empty_plates = int(D)
    pancakes_per_plate = [int(n) for n in Pi.split()]

    max_minutes = max(pancakes_per_plate)

    v = (pancakes_per_plate, 0)
    Q = deque([v])

    while Q:
        t = Q.popleft()

        current_pancakes = t[0]
        current_minutes = t[1]

        max_current_pancakes = max(current_pancakes)

        if max_current_pancakes is 0:
            return current_minutes

        vT = current_minutes + 1

        # try special
        v1Ps = make_it_special(current_pancakes, max_current_pancakes)
        if v1Ps:
            for v1P in v1Ps:
                Q.append((v1P, vT))

        # try eating
        v2P = eat_it(current_pancakes)
        Q.append((v2P, vT))

    return max_minutes


if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename) as input:
        T = int(input.readline())
        for case in range(0, T):
            D = input.readline()
            Pi = input.readline()
            output = solve(D, Pi)
            print "Case #%d: %s" % (case + 1, output)
