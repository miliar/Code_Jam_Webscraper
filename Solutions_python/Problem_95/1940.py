#!/usr/bin/python
import sys
mapping = [
    ('a', 'y'),
    ('b', 'n'),
    ('c', 'f'),
    ('d', 'i'),
    ('e', 'c'),
    ('f', 'w'),
    ('g', 'l'),
    ('h', 'b'),
    ('i', 'k'),
    ('j', 'u'),
    ('k', 'o'),
    ('l', 'm'),
    ('m', 'x'),
    ('n', 's'),
    ('o', 'e'),
    ('p', 'v'),
    ('q', 'z'),
    ('r', 'p'),
    ('s', 'd'),
    ('t', 'r'),
    ('u', 'j'),
    ('v', 'g'),
    ('w', 't'),
    ('x', 'h'),
    ('y', 'a'),
    ('z', 'q'),
]
def swapSides(a):#Takes 2 tuple
    return (a[1],a[0])
def decode(char):
    for i in range(0, len(mapping)):
        if(char == mapping[i][1]):
            return mapping[i][0]
    if(char >= 'a' and char <= 'z'):
        return '?'
    return char
def solve(line):
    ret = ""
    for i in range(0, len(line)):
        ret += decode(line[i])
    return ret
    
#Debug Mode
#
#for i in range(0, len(mapping)):
#    print mapping[i][0] + " -> " + mapping[i][1]
#mapping.sort(key=swapSides)
#for i in range(0, len(mapping)):
#    print mapping[i][1] + " <- " + mapping[i][0]

if len(sys.argv) != 3:
    print "Usage: tounges.py infile outfile"
    exit(1)
infile = open(sys.argv[1], "r")
outfile = open(sys.argv[2], "w")
lines = infile.readlines() 
N = int(lines[0])
for n in range(1, N+1):
    outfile.write("Case #"+str(n)+": " + solve(lines[n].strip())+"\n")
