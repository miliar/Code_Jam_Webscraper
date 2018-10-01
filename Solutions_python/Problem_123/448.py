#!/usr/bin/env python

import sys

def read(filename):
    """Yield a "test" chunk of lines from filename."""
    with open(filename, 'r') as f:
        num_tests = int(f.readline())
        for t in range(num_tests):
            num_lines = 2
            test = []
            for l in range(num_lines):
                test.append(f.readline())
            yield test

def munge(test_chunks):
    for chunk in test_chunks:
        armin, num_motes = [int(x) for x in chunk[0].split()]
        sizes = [int(x) for x in chunk[1].split()]
        assert num_motes == len(sizes)
        yield armin, num_motes, sizes

def format(index, result):
    """Format output properly."""
    output = "Case #%s: %s" % (index, result)
    return output

def find_eatable(armin, motes):
    if min(motes) < armin:
        eatable = max([x for x in motes if x < armin])
    else:
        eatable = None
    return eatable

def find_addable(armin, motes):
    if armin - 1 > 0 and find_eatable(armin + armin - 1, motes):
        return armin - 1
    else:
        return None

def solve(armin, motes):
    operations = 0
    while len(motes) > 0:
        # print armin, motes, operations
        # eat highest possible
        highest_eatable = find_eatable(armin, motes)
        if highest_eatable:
            motes.remove(highest_eatable)
            armin += highest_eatable
            continue

        # add highest possible (armin - 1)
        highest_addable = find_addable(armin, motes)
        if highest_addable:
            motes.append(highest_addable)
            operations += 1
            continue

        # Add highest possible, even if it can't eat next, as
        # long as there are > 2 motes remaining
        motes_len = len(motes)
        if len(motes) > 2 and armin - 1 > 0:
            sub_ops = solve(armin + armin - 1, motes)
            if sub_ops < motes_len:
                operations += 1
                motes = []
                operations += sub_ops
            else:
                motes = []
                operations += motes_len

        # remove remaining
        remaining = len(motes)
        motes = []
        operations += remaining

    return operations



def main(argv=None):
    if argv == None:
        argv = sys.argv

    if len(argv) != 2:
        sys.stderr.write("Usage: %s <input_file>" % argv[0])
        return 2

    infile = argv[1]
    raw = read(infile)
    munged = munge(raw)

    # print list(munged)

    for index, test in enumerate(munged):
        armin = test[0]
        motes = test[2]
        result = solve(armin, motes)
        print format(index + 1, result)

if __name__ == '__main__':
    main()



