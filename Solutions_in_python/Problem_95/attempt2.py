#!/usr/bin/env python

import sys
import string
import operator

def get_translator():
    mapping = {
        # Given
        'a': 'y', 
        'o': 'e',
        'z': 'q',
        ' ': ' ',

        # Determined manually
        'q': 'z',
    }
    sample = {
        "ejp mysljylc kd kxveddknmc re jsicpdrysi":
        "our language is impossible to understand",
        "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd":
        "there are twenty six factorial possibilities",
        "de kr kd eoya kw aej tysr re ujdr lkgc jv":
        "so it is okay if you want to just give up",
    }
    for ciphertext, plaintext in sample.items():
        for i in xrange(0, len(ciphertext)):
            mapping[ciphertext[i]] = plaintext[i]
    return mapping

def translate(line, mapping):
    return "".join(map(lambda x: mapping[x], line))

if __name__ == "__main__":
    mapping = get_translator()

    # Read & process tests
    tests = []
    numtests = int(sys.stdin.readline())
    for i in xrange(0, numtests):
        tests.append(sys.stdin.readline().rstrip())

    for i in xrange(0, numtests):
        print "Case #%d: %s" % (i+1, translate(tests[i], mapping))

# vim:set expandtab tabstop=4 shiftwidth=4 softtabstop=4 nowrap:

