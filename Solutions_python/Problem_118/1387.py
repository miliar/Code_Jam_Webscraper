from math import sqrt

def ispalin(n):
    ninin = str(n)[::-1]
    return n == int(ninin)

def sqrange(start, stop):
    sqlist = range(int(sqrt(start)), int(sqrt(stop))+1)
    
    # square stuff
    for xen in range(len(sqlist)):
        sqlist[xen] = sqlist[xen]*sqlist[xen]
    
    # valid head?
    if sqlist[0] < start:
        sqlist = sqlist[1:]
    
    return sqlist

def sumfairsquares(alist):
    sum = 0
    
    for item in alist:
        sum += (ispalin(item) and ispalin(int(sqrt(item))))
    
    return sum

###############################################################################

# get files
name = raw_input() # name of file without .in suffix
f = open(name+".in", 'r')
g = open(name+".out", 'w')

# get cases
cases = int(f.readline())
i = 0
while i < cases:
    # get [a, b]
    values = f.readline().split()
    a = int(values[0])
    b = int(values[1])
    
    # solve
    g.write("Case #%d: %d\n" % (i+1, sumfairsquares(sqrange(a, b))))
    
    # progress
    i += 1

f.close()
g.close()
