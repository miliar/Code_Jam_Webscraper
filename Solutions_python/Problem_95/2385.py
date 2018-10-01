#!/usr/bin/env python
import sys

i1, o1 = ("ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand")
i2, o2 = ("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities")
i3, o3 = ("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up")
i4, o4 = ("qz", "zq")

def translate(stmt, mtable):
    output = ""
    for i in stmt:
        output = output + mtable[i]
    return output

def create_table(mtable, pairs):
    for key_string, val_string in pairs:
        for i, j in zip(key_string, val_string):
            mtable[i] = j

    return mtable


if __name__ == '__main__':
    pairs = [
        (i1, o1), (i2, o2), (i3, o3), (i4, o4),
        ]
    mtable = create_table({}, pairs)
    
    inputs = open(sys.argv[1]).readlines()
    outputs = open(sys.argv[2], "w")

    for i, line in enumerate(inputs):
        if i != 0:
            line = line.strip()
            output = "Case #%s: %s\n" % (i, translate(line, mtable))
            outputs.write( output )

            print output.strip()
        
