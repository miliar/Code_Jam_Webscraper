#!/usr/bin/python

dictionary = { 'y': 'a',
               'n': 'b',
               'f': 'c',
               'i': 'd',
               'c': 'e',
               'w': 'f',
               'l': 'g',
               'b': 'h',
               'k': 'i',
               'u': 'j',
               'o': 'k',
               'm': 'l',
               'x': 'm',
               's': 'n',
               'e': 'o',
               'v': 'p',
               'z': 'q',
               'p': 'r',
               'd': 's',
               'r': 't',
               'j': 'u',
               'g': 'v',
               't': 'w',
               'h': 'x',
               'a': 'y',
               'q': 'z'}

def translate(text):
    result = ''
    for c in text:
        if c.lower() in dictionary:
            tr_c = dictionary[c.lower()]
            if c.isupper():
                tr_c = tr_c.upper()
        else:
            tr_c = c
        result += tr_c
    return result

with open('A-small-attempt0.in') as f:
    nb = int(f.readline())
    i = 1
    for line in f.readlines():
        print "Case #%d: %s" % (i, translate(line[:-1]))
        i += 1

