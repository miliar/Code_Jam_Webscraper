# Hints
# a -> y
# o -> e
# z -> q

import string
import sys

table = {}
hints = [
    ('y qee', 'a zoo'),
    ('ejp mysljylc kd kxveddknmc re jsicpdrysi', 'our language is impossible to understand'),
    ('rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd', 'there are twenty six factorial possibilities'),
    ('de kr kd eoya kw aej tysr re ujdr lkgc jv', 'so it is okay if you want to just give up'),
    # only character mapping not deterimed by the hints is 'z' -> 'q'
    ('z', 'q')
    ]

def extract_from_hints():
    for hint in hints:
        for char in zip(hint[0], hint[1]):
            googlerese = char[0]
            english = char[1]
            if (english.isalpha()):
                table[googlerese] = english

def print_table(table):
    mapped = set()
    used = set()
    for key in sorted(table.iterkeys()):
        mapped.add(key)
        used.add(table[key])
        print '%s: %s' % (key, table[key])

    print 'Not mapped: %s' % (set(string.lowercase) - mapped)
    print 'Not used: %s' % (set(string.lowercase) - used)

def solve_case(googlerese):
    english = str()
    for char in googlerese:
        if char.isalpha():
            english += table[char]
        elif char == ' ':
            english += char
    return english

extract_from_hints()
num_cases = int(sys.stdin.readline())

for i, line in zip(range(1, num_cases + 1), sys.stdin):
    print 'Case #%d: %s' % (i, solve_case(line))
