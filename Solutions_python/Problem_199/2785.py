import sys


def flip_pancake(state):
    return '-' if state == '+' else '+'


# Flip count pancakes starting at index
def flip(pancakes, index, count):
    if index + count > len(pancakes) or index < 0:
        raise ValueError("Flipping invalid pancakes. Index %d, Count %d" % (index, count))
    for i in xrange(index, index + count):
        pancakes[i] = flip_pancake(pancakes[i])


def is_all_happy(pancakes):
    return pancakes[0] == '+' and len(set(pancakes)) == 1


# Search for the first - and flip k pancakes. Repeat until end.
def get_min_flip_count(pancakes, k):
    # print "Initial", pancakes
    num_flips = 0
    for i in xrange(len(pancakes) - k + 1):
        if pancakes[i] == '-':
            flip(pancakes, i, k)
            # print "Flipped %d pancakes at index %d" % (k, i), pancakes
            num_flips += 1
    if is_all_happy(pancakes):
        return num_flips
    else:
        return "IMPOSSIBLE"


def main(filename):
    # print "Reading from: ", filename
    with open(filename) as f:
        num_entries = int(f.readline())
        for i in range(num_entries):
            pancakes, k = f.readline().split()
            solution = get_min_flip_count(list(pancakes), int(k))
            print "Case #" + str((i + 1)) + ": " + str(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "You should provide the input file name"
    else:
        main(sys.argv[1])