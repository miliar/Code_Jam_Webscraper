'''
Created on May 7, 2011

@author: herman
'''

from string import split

infile = open("large_input.txt","r")
outfile = open("large_output.txt","w")

trials = int(infile.readline())

def cycleCount(lst):
    traversed = [False for x in xrange(len(lst))]
    cycles = []
    tindex = 0
    while tindex < len(traversed):
        if not traversed[tindex]:
            count = 1
            start = tindex
            traversed[start] = True
            next = lst[start]
            while start != next:
                traversed[next] = True
                next = lst[next]
                count += 1
            cycles.append(count)
        tindex += 1
    return cycles
        

for i in xrange(trials):
    nums = int(infile.readline())
    vals = [int(x) for x in split(infile.readline())]
    vals.insert(0,0)
    
    cvals = cycleCount(vals)
    total = 0
    for x in cvals:
        if x > 1:
            total += x
    s = "Case #%d: %d\n" %((i+1),total)
    outfile.write(s)
    print s
    

infile.close()
outfile.close()