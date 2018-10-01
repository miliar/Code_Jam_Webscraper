#!/usr/bin/pypy

def recycledNumbers(start):
    n = len(start)
    return [start[i:] + start[0:i] for i in range(1,n)]

def isRecycledPair(p):
    return str(p[1]) in recycledNumbers(str(p[0]))

def recycledPairsInRange(a,b):
    i=0
    for n in range(a,b+1): 
        for m in range(n+1,b+1):
            if isRecycledPair((n,m)):
                i+=1
    return i

def main():
    fin = open("input.txt")
    fout = open("output.txt", 'w')
    i = 0 
    for line in fin:
        if i == 0:
            l = int(line)
        elif i == l+1:
            break
        else:
            nums = map(int,line.split())
            n = recycledPairsInRange(nums[0], nums[1])
            fout.write("Case #%i: %i\n" % (i,n))
        i+=1

main()
