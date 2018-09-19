#!/usr/bin/python2
#A = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
#     'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ',
#     '.', ',', ';', ':', "'", '!', '?']

A = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
     'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

import json
import sys

def rimuovi_perm(testo, perm):
    chiaro = ""
    for l in testo:
        if l not in A:
            chiaro += l
            continue
        l_decr = perm[l]
        chiaro += l_decr
    return chiaro

if __name__ == "__main__":
    #with open(sys.argv[1]) as f:
    #    cifrato = f.read()
    #perm = json.loads(open(sys.argv[2]).read())
    perm = json.loads(open('perm.txt').read())

    out = ""

    with open(sys.argv[1]) as f:
        for i, cifrato in enumerate(f):
            if i == 0: 
                continue
            out += "Case #%i: " % i
            out += rimuovi_perm(cifrato, perm)
    
    print out,
    
    with open('output','w') as f:
        print>>f, out,
