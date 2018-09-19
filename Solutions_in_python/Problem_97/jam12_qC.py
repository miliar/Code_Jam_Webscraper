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

ns = [1,2,3,4,5,6,7,8,9]

def getans(f,t):
    count = 0
    cnts = {}
    seqs = []
    digits = set([])
    for i in range(f,t+1):
        seqs.append(str(i))
    #print seqs
    dones = []
    for seq in seqs:
        if seq in dones:
            continue
        cnts[seq] = 0
        for j in range(len(seq)):
            digit = seq[j:] + seq[:j]
            if digit in seqs:
                if digit in dones:
                    continue
                dones.append(digit)
                cnts[seq] += 1
    #print cnts
    for s,cnt in cnts.iteritems():
        if cnt >0:
            count += cnt * (cnt - 1) /2
    return count

def main():
    f = open(sys.argv[1])
    fo = open(sys.argv[2],"w")

    cases = int(f.readline().strip())
    for i in range(cases):
        l = [int(x) for x in f.readline().strip().split()]
        fr = l[0]
        t = l[1]
        out = "Case #%d: %s"%(i+1,getans(fr,t)) + "\n"
        print out,
        fo.write(out)
    f.close()
    fo.close()

if __name__ == '__main__':
    main()
