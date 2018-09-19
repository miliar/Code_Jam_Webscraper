#!/usr/bin/python
from pprint import pprint
import string
import itertools

# example input
pairs = [
    ('ejp mysljylc kd kxveddknmc re jsicpdrysi',
    'our language is impossible to understand'),

    ('rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
    'there are twenty six factorial possibilities'),

    ('de kr kd eoya kw aej tysr re ujdr lkgc jv',
    'so it is okay if you want to just give up'),
]


def setup_mapping(pairs):
    mapping = {}
    for left, right in pairs:
    	for l,r in zip(left,right):
    		mapping[l] = r

    # tricky.
    mapping['z'] = 'q'
    mapping['q'] = 'z'

    return mapping

def read_input_lines(stream):
    """Read lines from input stream, skipping the first line."""
    for line in itertools.islice(stream.readlines(), 1, None):
        clean_line = line.strip()
        if clean_line:
            yield clean_line

def translate(googlerese, mapping):
    return "".join(map(lambda x: mapping[x], googlerese))

def report(n, answer):
    print "Case #{}: {}".format(n, answer)

if __name__ == '__main__':
    import sys
    mapping = setup_mapping(pairs)
    for case_number, input_line in enumerate(read_input_lines(sys.stdin), start=1):
        english = translate(input_line, mapping)
        report(case_number, english)
