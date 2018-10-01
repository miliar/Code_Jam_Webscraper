#!/usr/local/Cellar/python3/3.2.2/bin/python3

from GCJ import GCJ
import math

g = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv y qee z"   
e = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up a zoo q"

def solve(infile):
    code  = GCJ.readstr(infile) 
    trans = { a:e[g.index(a)] for a in "abcdefghijklmnopqrstuvwxyz"}
 
    res = ""
    for ch in code:
        try:
            res += trans[ch]
        except:
            res += ch
    return res
    
if __name__ == "__main__":
    GCJ("A", solve).run()
