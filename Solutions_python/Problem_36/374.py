#!/usr/bin/python
#Welcome to Code Jam
#ALG: filter out unused letters, then DP
#DP: possibilties from index i (so far) = possibilties for i already + possibilities for i+1 so far. Goes backwards through string
#But we don't work on a string, we work on a preprocessed list. The list is like the characters in order, but with their index replacing their char. For characters that occur multiple times they are replaced by all their indices, in descending order (though that doesn't really matter). It is also processed so that every member can be used, not that I know if that's needed.

import sys
#Repeats: ecom
STR = 'welcome to code jam'
#      0123456789012345678
#vals replaces a letter with it's indices
vals = {
    'a':[17],
    'c':[11,3],
    'd':[13],
    'e':[14,6,1],
    'j':[16],
    'l':[2],
    'm':[18,5],
    'o':[12,9,4],
    't':[8],
    'w':[0],
    ' ':[15,10,7]
}
DP = []

def init(string):
    global DP,STR
    """Inits DP and turns string into list"""
    DP = []
    for a in STR:
        DP.append(0)
    DP.append(1)
    ret = []
    for a in string:
        if a in vals:
            ret += vals[a]
    return ret

def doDP(inp):
    #inp is the processed list
    acc = len(inp)
    while(acc > 0):
        acc -= 1
        val = inp[acc]
        DP[val] += DP[val+1]
        DP[val] %= 10000 #4 digit constraint

def solve(string):
    processed = init(string)
    doDP(processed)
    return '%04d'%DP[0]

#Main
for i in STR:
    DP.append(0)
DP.append(1)
N = int(sys.stdin.readline())
acc = 0
for line in sys.stdin.readlines():
    acc += 1
    print("Case #"+str(acc)+": "+solve(line.rstrip()))
    
