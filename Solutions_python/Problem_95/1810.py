# -*- coding: utf-8 -*-

import sys
fin = sys.stdin
T = int(fin.readline())

l = {}

def add_rosetta(a,b):
    for aa,bb in zip(a,b):
        l[aa] = bb

add_rosetta('ejp mysljylc kd kxveddknmc re jsicpdrysi', 'our language is impossible to understand')        
add_rosetta('rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd', 'there are twenty six factorial possibilities')
add_rosetta('de kr kd eoya kw aej tysr re ujdr lkgc jv', 'so it is okay if you want to just give up')
add_rosetta('y qee', 'a zoo')

def fix_missing():
    l1 = 'abcdefghijklmnopqrstuvwxyz'
    for aa in l.keys():
        l1 = l1.replace(aa, '')
    
    l2 = 'abcdefghijklmnopqrstuvwxyz'
    for aa in l.values():
        l2 = l2.replace(aa, '')
    
    l[l1] = l2

fix_missing()
    
def translate(a):
    r = ""
    for aa in a:
        r += l[aa]
                
    return r

for case in range(1,T+1):    
    print "Case #%d: %s" % (case, translate(fin.readline().replace('\n', '')))