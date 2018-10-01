#!/usr/bin/env python

sub = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o' : 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z' : 'q', 'u' : 'j', 'g' : 'v'}

if __name__ == "__main__":
    for i in xrange(int(raw_input())):
        print "Case #%d: %s" % (i + 1, ''.join(sub.get(c, ' ') for c in raw_input()))
    letters = ''.join(chr(i) for i in xrange(ord('a'), ord('z') + 1))
