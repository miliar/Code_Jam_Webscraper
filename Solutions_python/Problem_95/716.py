#!/usr/bin/python


d = dict([('a', 'y'),
    ('b', 'h'),
    ('c', 'e'),
    ('d', 's'),
    ('e', 'o'),
    ('f', 'c'),
    ('g', 'v'),
    ('h', 'x'),
    ('i', 'd'),
    ('j', 'u'),
    ('k', 'i'),
    ('l', 'g'),
    ('m', 'l'),
    ('n', 'b'),
    ('o', 'k'),
    ('p', 'r'),
    ('q', 'z'),
    ('r', 't'),
    ('s', 'n'),
    ('t', 'w'),
    ('u', 'j'),
    ('v', 'p'),
    ('w', 'f'),
    ('x', 'm'),
    ('y', 'a'),
    ('z', 'q'),
    (' ', ' '),
    ('\n','')])

def get_input(input_file):
    
    f = open(input_file,'r')
    T = int(f.readline())

    for t in range(T):
        s = f.readline()
        res = ""
        for sub in s:
            res+= d[sub]
        print 'Case #%d: %s'%(t+1,res)

if __name__ == "__main__": 
    import sys
    input_file = str(sys.argv[1])

    get_input(input_file)
