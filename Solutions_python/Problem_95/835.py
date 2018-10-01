# -*- coding: utf-8 -*-

import sys

def make_trans_dict():
    all_alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    cypher = """
    ejp mysljylc kd kxveddknmc re jsicpdrysi
    rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
    de kr kd eoya kw aej tysr re ujdr lkgc jv
    """
    
    clear = """
    our language is impossible to understand
    there are twenty six factorial possibilities
    so it is okay if you want to just give up
    """
    
    trans_dict = {}
    
    for i in range(len(cypher)):
        ch_cypher = cypher[i]
        ch_clear = clear[i]
        if not ch_cypher in trans_dict:
            trans_dict[ch_cypher] = ch_clear

    trans_dict['z'] = 'q'
    trans_dict['q'] = 'z'
            
    return trans_dict
    
def is_alphabet(ch):
    return ord('a') <= ord(ch) <= ord('z')

trans_dict = make_trans_dict()
def translate(line):
    ans = ""
    for ch in line:
        if is_alphabet(ch):
            ans += trans_dict[ch]
        else:
            ans += ch
    return ans

limit = int(sys.stdin.readline())
for count in range(limit):
    line = sys.stdin.readline()
    print "Case #" + str(count+1) + ": " + translate(line),

    

    

