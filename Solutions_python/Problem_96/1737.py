#!/usr/bin/python
import sys,math
def solve(line):
    nums = map(int, line.split(' '))
    G = nums[0]
    S = nums[1]
    p = nums[2]
    #print G,S,p,nums[3:]
    ret = 0 #number >= p
    sp = 0 #number of ones boosted
    for i in range(3, 3 + G):
        t = nums[i]
        a = math.ceil(t/3.0)
        #print t,a
        if a >= p:
            ret += 1
            continue
        if sp < S and a == p-1 and (t%3) != 1 and a not in [0,10]:
            ret += 1
            sp += 1
    return str(ret)

if len(sys.argv) != 3:
    print "Usage: "+ sys.argv[0]  +" infile outfile"
    exit(1)
infile = open(sys.argv[1], "r")
outfile = open(sys.argv[2], "w")
lines = infile.readlines() 
N = int(lines[0])
for n in range(1, N+1):
    outfile.write("Case #"+str(n)+": " + solve(lines[n].strip())+"\n")
