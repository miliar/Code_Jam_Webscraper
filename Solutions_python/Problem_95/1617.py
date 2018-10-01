#! /usr/bin/python -tt
import sys

mapping = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'q': 'z', 'z': 'q'}

def googlerese(text):
    ret = []
    for ch in text:
        ret.append(mapping[ch])
    return ''.join(ret)

def ReadInts(f):
    return map(int, list(f.readline().strip()))
def ReadChars(f):
    return f.readline().strip()

f = open(sys.argv[1], 'r')
t = int(f.readline().strip())
for i in xrange(1, t+1):
    line = ReadChars(f)
    outp = googlerese(line)
    print "Case #%d: %s" % (i, outp)
