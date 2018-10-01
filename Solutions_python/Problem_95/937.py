#!/usr/bin/python

import string
import sys

def derive_mapping(input, output):
    return {i : o for i,o in zip(input, output) if i.isalpha()}

def complete_table(initial_mapping):
    if len(initial_mapping) < 26:
        for i, o in zip(set(string.lowercase) - set(initial_mapping.keys()), set(string.lowercase) - set(initial_mapping.values())):
            initial_mapping[i] = o
    return string.maketrans("".join(initial_mapping.keys()), "".join(initial_mapping.values()))


if __name__ == "__main__":
    example_in = "y qee ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
    example_out = "a zoo our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"
    transtab = complete_table(derive_mapping(example_in, example_out))

    with open(sys.argv[1]) as f:
        count = int(f.readline())
        for i in range(1, count + 1):
            print "Case #%d: %s" % (i, f.readline().strip().translate(transtab))
