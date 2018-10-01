#!/usr/bin/python
import sys

def solve(strings):
    seq = None
    vals = []
    for i, string in enumerate(strings):
        valIndex = -1
        if seq is None:
            seq = []
            last = None
            for c in string:
                if c != last:
                    seq.append(c)
                    vals.append([1])
                    valIndex += 1
                    last = c
                else:
                    vals[valIndex][i] += 1
            #print "seq init", seq
        else:
            last = None
            for c in string:
                if c != last and (valIndex == len(seq)-1 or seq[valIndex+1] != c):
                    return "Fegla Won"
                elif c != last:
                    valIndex += 1
                    # Check for overrun (if first is subseq of second)
                    if (valIndex == len(seq)):
                        print "Overrun"
                        return "Fegla Won"
                    vals[valIndex].append(1)
                    last = c
                else:
                    vals[valIndex][i] += 1
            # Check for underrun (if second is subseq of first)
            if (valIndex != len(seq)-1):
                return "Fegla Won"
    total = 0
    for valList in vals:
        mid = len(valList)/2
        midVal = sorted(valList)[mid]
        for val in valList:
            total += abs(midVal-val)
    return total

T = int(sys.stdin.readline())
for i in xrange(T):
    print "Case #%d:" % (i+1),
    N = int(sys.stdin.readline().strip())
    strings = []
    for j in xrange(N):
        string = sys.stdin.readline().strip()
        strings.append(string)
    print solve(strings)
