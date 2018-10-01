#!/usr/local/bin/pypy
import sys
import itertools

# Config.
attempt = 0

# Constants.
INFILE = 'A-large-%s.in' % attempt
OUTFILE = 'A-large-%s.out' % attempt

# Program.

content = [line.strip().split(' ') for line in open(INFILE).readlines()][1:]
output = open(OUTFILE, 'w')

def answer(oranges, blues, pairs):
    o = 1
    b = 1
    t = 0
    
    while len(pairs) != 0:
        t += 1
        
        topop = False
        
        pair = pairs[0]
        name = pair[0]
        pos = int(pair[1])
        curpos = (o if name == 'O' else b)
        if curpos == pos:
            pairs.pop(0)
            topop = True
        
        if len(oranges) != 0: o = o + cmp(oranges[0], o)
        if len(blues) != 0: b = b + cmp(blues[0], b)
        # The above will give +1, 0 or -1
        
        if topop: (oranges if name == 'O' else blues).pop(0)
    return t

case = 0
for line in content:
    case += 1
    
    orange = []
    blue = []
    
    line.pop(0)
    pairs = [(line[i], line[i+1]) for i in xrange(0, len(line) - 1, 2)]
    
    for pair in pairs:
        if pair[0] == 'O':
            orange.append(int(pair[1]))
        else:
            blue.append(int(pair[1]))
    
    output.write("Case #%s: %s\n" % (case, answer(orange, blue, pairs)))