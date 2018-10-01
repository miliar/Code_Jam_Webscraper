#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      wani
#
# Created:     14/04/2012
# Copyright:   (c) wani 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import sys
import copy

def getans(N,S,p,totals):
    ans = 0
    pairs =[]
    for total in totals:
        if total % 3 == 0:
            max = total / 3
        else:
            max = total / 3 + 1
        pairs.append([max,total])
    pairs.sort()
    for pair in pairs:
        if pair[0] >= p:
            ans += 1
        elif pair[0] == p-1 and pair[1]%3 != 1 and pair[1] > 1 and S >0:
            ans += 1
            S -= 1
    return ans

def main():
    f = open(sys.argv[1])
    fo = open(sys.argv[2],"w")

    cases = int(f.readline().strip())
    for i in range(cases):
        l = [int(x) for x in f.readline().strip().split()]
        N = l[0]
        S = l[1]
        p = l[2]
        totals = l[3:]
        out = "Case #%d: %s"%(i+1,getans(N,S,p,totals)) + "\n"
        print out,
        fo.write(out)
    f.close()
    fo.close()

if __name__ == '__main__':
    main()
