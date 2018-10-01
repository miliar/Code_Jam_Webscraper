#!/bin/python

import sys

dico = {'y':'a', 'e':'o', 'q':'z', 'z': 'q'}
s1="ejp mysljylc kd kxveddknmc re jsicpdrysi"
s2="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
s3="de kr kd eoya kw aej tysr re ujdr lkgc jv"
r1="our language is impossible to understand"
r2="there are twenty six factorial possibilities"
r3="so it is okay if you want to just give up"

for i in range(len(s1)):
    dico[s1[i]] = r1[i]
for i in range(len(s2)):
    dico[s2[i]] = r2[i]
for i in range(len(s1)):
    dico[s3[i]] = r3[i]
T = int(sys.stdin.readline())
for i in range(T):
    res = ''
    line = sys.stdin.readline()
    for j in line[:len(line)-1]:
        res += dico[j]
    print('Case #{0}: {1}'.format(i+1, res))

