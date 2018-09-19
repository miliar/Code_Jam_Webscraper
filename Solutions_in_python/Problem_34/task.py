import sys
#from numpy import *
from datetime import datetime

print datetime.now()
#iFName = "d:\\projekty\\google-jam\\runda-2\\c\\A-small.in"
#iFName = "a.txt"
#iFName = "A-small-attempt0.in"
iFName = "A-large.in"
outFN = "out.txt"

iFile = open(iFName, "r")
outF =  open(outFN, "w")

verbose = False

#how many cases?
S =  iFile.readline()
print S
S = S.split()
if verbose:
    print S
L = int(S[0])
D = int(S[1])
N = int(S[2])

if verbose:
    print L, D, N
    
dic = {}
for i in range (L):
    for j in "abcdefghijklmnopqrstuvwxyz":
        dic[(i, j)] = set([])
        
#read the set of words
for case in range(D) :
    word = iFile.readline()
    if verbose:
        print case
        print word
    for i in xrange(len(word) - 1):
        dic[(i, word[i])].add(case)

if verbose:
    for i in dic:
        if dic[i] <> set([]):
            print i, dic[i]
            
#read the test cases
for case in range(N) :
    print case, datetime.now()
    res = set(range(D))
    if verbose:
        print res
    if verbose:
        print case
    mask = iFile.readline()
    if verbose:
        print mask
    add = False
    idx = 0
    for i in xrange(len(mask) - 1):
        if mask[i] == '(':
            ast = set([])
            add = True
        elif mask[i] == ')':
            res &= ast
            add = False
            idx += 1
        else:
            if add :
                ast |= dic[(idx, mask[i])]
            else:
                res &= dic[(idx, mask[i])]
                idx += 1
        
    if verbose:
        print "Case #%(c)d: %(cnt)d" % {'c' : case + 1, 'cnt' : len(res)}
    print >> outF , "Case #%(c)d: %(cnt)d" % {'c' : case + 1, 'cnt' : len(res)}

iFile.close()
outF.close()
print datetime.now()
